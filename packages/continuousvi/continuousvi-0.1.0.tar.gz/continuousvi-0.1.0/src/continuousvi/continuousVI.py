"""ContinuousVI module for scRNA-seq data analysis.

This module provides classes and methods to train and utilize scVI models for
single-cell RNA-seq data. It supports the inclusion of continuous covariates
(e.g., pseudotime in trajectory analysis, aging or other continuous measurements) while correcting for batch
effects. The main classes are:

- ContinuousVI: Sets up the anndata object and trains multiple scVI models.
- TrainedContinuousVI: Manages one or more trained scVI models, provides methods
  for generating embeddings, sampling expression parameters, and performing
  regression analysis.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import TYPE_CHECKING, Literal, Optional, overload

import numpy as np
import pandas as pd
import patsy
import scanpy as sc
import scvi
import statsmodels.api as sm
import torch
from tqdm import tqdm

if TYPE_CHECKING:
    from scvi.distributions import ZeroInflatedNegativeBinomial


class ContinuousVI:
    """ContinuousVI module for scRNA-seq data analysis.

    This class is responsible for configuring the input data (AnnData object)
    and training multiple scVI models to account for batch effects, label keys,
    and one optional continuous covariate. Use the `train` method to train
    multiple scVI models. The trained models can be accessed via the returned
    `TrainedContinuousVI` instance.
    """

    def __init__(
        self,
        adata: sc.AnnData,
        batch_key: str,
        label_key: str | None,
        continuous_key: str | None,
    ) -> None:
        """Initialize a ContinuousVI object.

        Parameters
        ----------
        adata : sc.AnnData
            The annotated data matrix with cells (observations) and genes (variables).
        batch_key : str
            The column name in `adata.obs` that contains batch information.
        label_key : str or None
            The column name in `adata.obs` that contains label or cell-type information.
            If None, no label covariate is used.
        continuous_key : str or None
            The column name in `adata.obs` that contains a single continuous covariate
            (e.g., pseudotime). If None, no continuous covariate is used.

        """
        self.adata: sc.AnnData = adata
        self.batch_key: str = batch_key
        self.label_key: str | None = label_key
        self.continuous_key: str | None = continuous_key

    def train(
        self,
        n_train: int = 5,
        n_latent: int = 30,
        max_epochs: int = 800,
        early_stopping: bool = True,
    ) -> TrainedContinuousVI:
        """Train multiple scVI models (n_train times) and return a TrainedContinuousVI object.

        This method sets up the scVI anndata configuration once per training run
        and trains `n_train` scVI models with the same hyperparameters but
        potentially different random initializations.

        Parameters
        ----------
        n_train : int, default=5
            The number of times to train scVI with the same setup.
        n_latent : int, default=30
            The dimensionality of the scVI latent space (z).
        max_epochs : int, default=800
            The maximum number of training epochs.
        early_stopping : bool, default=True
            Whether to apply early stopping based on validation loss improvements.

        Returns
        -------
        TrainedContinuousVI
            A TrainedContinuousVI object containing the trained scVI models,
            allowing further analysis and model usage.

        """
        _trained_models: list[scvi.model.SCVI] = []
        for _ in tqdm(
            range(n_train),
            desc="Training multiple scVI models",
            leave=False,
        ):
            scvi.model.SCVI.setup_anndata(
                self.adata,
                batch_key=self.batch_key,
                labels_key=self.label_key,
                continuous_covariate_keys=[self.continuous_key]
                if self.continuous_key
                else None,
            )
            model = scvi.model.SCVI(self.adata, n_latent=n_latent)
            model.train(max_epochs=max_epochs, early_stopping=early_stopping)
            _trained_models.append(model)
        return TrainedContinuousVI(
            adata=self.adata,
            batch_key=self.batch_key,
            label_key=self.label_key,
            continuous_key=self.continuous_key,
            trained_models=_trained_models,
        )


class TrainedContinuousVI:
    """TrainedContinuousVI manages one or more trained scVI models for scRNA-seq data.

    This class provides methods to:
    - Load or store multiple trained scVI models.
    - Calculate embeddings (UMAP, clusters) using the latent representation.
    - Perform regressions against the continuous covariate.
    - Sample parameters from the generative model (px).
    - Save the trained models to disk.
    """

    @overload
    def __init__(
        self,
        adata: sc.AnnData,
        batch_key: str,
        label_key: str | None,
        continuous_key: str | None,
        trained_models: list[scvi.model.SCVI],
    ) -> None: ...

    @overload
    def __init__(
        self,
        adata: sc.AnnData,
        batch_key: str,
        label_key: str | None,
        continuous_key: str | None,
        trained_model_path: Path | str,
    ) -> None: ...

    def __init__(
        self,
        adata: sc.AnnData,
        batch_key: str,
        label_key: str | None,
        continuous_key: str | None,
        trained_models: list[scvi.model.SCVI] | None = None,
        trained_model_path: Path | str | None = None,
    ) -> None:
        """Initialize a TrainedContinuousVI object with trained scVI models or a path to load them.

        Parameters
        ----------
        adata : sc.AnnData
            The annotated data matrix used for model training or inference.
        batch_key : str
            The column name in `adata.obs` for batch information.
        label_key : str or None
            The column name in `adata.obs` for label or cell-type information.
        continuous_key : str or None
            The column name in `adata.obs` for continuous covariate information.
        trained_models : list[scvi.model.SCVI], optional
            A list of scVI models that have already been trained.
        trained_model_path : Path or str, optional
            Path to a directory that contains one or more trained scVI models.
            If provided, the models at this path will be loaded instead of using
            `trained_models`.

        Raises
        ------
        ValueError
            If both `trained_models` and `trained_model_path` are None.

        """
        self.adata = adata
        self.batch_key: str = batch_key
        self.label_key: str | None = label_key
        self.continuous_key: str | None = continuous_key

        scvi.model.SCVI.setup_anndata(
            adata=adata,
            batch_key=batch_key,
            labels_key=label_key,
            continuous_covariate_keys=[continuous_key]
            if continuous_key is not None
            else None,
        )

        if trained_models is None and trained_model_path is None:
            raise ValueError(
                "`trained_models` or `trained_model_path` is required. Both are None.",
            )

        if trained_models is None and trained_model_path is not None:
            _trained_model_paths = [
                p
                for p in (
                    trained_model_path
                    if isinstance(trained_model_path, Path)
                    else Path(trained_model_path)
                ).rglob("*")
                if p.is_dir()
            ]
            _trained_models: list[scvi.model.SCVI] = [
                scvi.model.SCVI.load(str(p), adata)
                for p in tqdm(_trained_model_paths, desc="Loading pre-trained models")
            ]
        else:
            _trained_models = trained_models

        self.trained_models = _trained_models

        self._embeddings: TrainedContinuousVI.Embeddings | None = None

    @property
    def embeddings(self) -> TrainedContinuousVI.Embeddings:
        """Return the Embeddings object for visualizations and further downstream analyses.

        Returns
        -------
        TrainedContinuousVI.Embeddings
            An Embeddings object that provides methods such as `umap` for
            generating UMAP plots.

        Raises
        ------
        ValueError
            If embeddings have not been computed yet. Please call
            `calc_embeddings()` first.

        """
        if self._embeddings is None:
            raise ValueError(
                "No Embeddings object found. Please execute `calc_embeddings()` first."
            )
        return self._embeddings

    def latent_coord(self, n_use_model: int = 0) -> np.ndarray:
        """Return the latent coordinates from one of the trained scVI models.

        Parameters
        ----------
        n_use_model : int, default=0
            The index of the trained model in `self.trained_models` to use for
            obtaining the latent representation.

        Returns
        -------
        numpy.ndarray
            A 2D array of shape (n_cells, n_latent) containing the latent representation.

        """
        arr: np.ndarray = self.trained_models[n_use_model].get_latent_representation(
            adata=self.adata,
        )
        return arr

    def calc_embeddings(
        self,
        resolution: float = 0.5,
        n_neighbors: int = 10,
        n_pcs: int = 30,
        n_use_model: int = 0,
    ) -> TrainedContinuousVI:
        """Calculate embeddings and cluster labels using the latent space.

        This method:
        - Stores the latent coordinates in `adata.obsm["X_latent"]`.
        - Computes neighborhood graphs using `scanpy.pp.neighbors`.
        - Performs draw_graph, leiden clustering, paga, and UMAP embedding.
        - Creates an `Embeddings` object that can be used for plotting.

        Parameters
        ----------
        resolution : float, default=0.5
            Resolution parameter for the leiden clustering. Higher values lead to
            more granular clustering.
        n_neighbors : int, default=10
            Number of neighbors to use for building the k-NN graph.
        n_pcs : int, default=30
            Number of principal components to use for neighborhood computation (if applicable).
        n_use_model : int, default=0
            The index of the trained model to use when extracting latent coordinates.

        Returns
        -------
        TrainedContinuousVI
            The TrainedContinuousVI instance with updated embeddings in `adata.obsm`
            and a newly created `Embeddings` object (`self._embeddings`).

        """
        KEY_LATENT = "X_latent"
        KEY_CLUSTER = "clusters"
        self.adata.obsm[KEY_LATENT] = self.latent_coord(n_use_model)
        sc.pp.neighbors(
            self.adata, n_neighbors=n_neighbors, n_pcs=n_pcs, use_rep=KEY_LATENT
        )
        sc.tl.draw_graph(self.adata)
        sc.tl.leiden(
            self.adata, key_added=KEY_CLUSTER, resolution=resolution, directed=False
        )
        sc.tl.paga(self.adata, groups=KEY_CLUSTER)
        sc.tl.umap(self.adata)
        self._embeddings = TrainedContinuousVI.Embeddings(self)
        return self

    def save(
        self,
        dir_path: Path | str,
        overwrite: bool = False,
    ) -> TrainedContinuousVI:
        """Save the trained models to the specified directory.

        Each model is saved in a subdirectory named `model_{i}` where `i`
        is the index of the model. For example, if there are 5 models in
        `self.trained_models`, subdirectories `model_0, model_1, ... model_4`
        will be created.

        Parameters
        ----------
        dir_path : Path or str
            The directory path where the models will be saved.
        overwrite : bool, default=False
            Whether to overwrite existing models at the target path if a
            model directory already exists.

        Returns
        -------
        TrainedContinuousVI
            The TrainedContinuousVI instance (self) for chained operations.

        """
        _base_path = dir_path if isinstance(dir_path, Path) else Path(dir_path)
        for n in tqdm(range(len(self.trained_models)), desc="Saving trained model."):
            _path = _base_path / Path(f"model_{n}")
            self.trained_models[n].save(_path, overwrite=overwrite)
        return self

    def sample_px(self, transform_batch: int = 0, n_draws: int = 25) -> torch.Tensor:
        """Sample px (the distribution parameters for the gene expression) from trained models.

        The px distribution is the Zero-Inflated Negative Binomial (ZINB) or
        Negative Binomial in scVI, depending on configuration. This method samples
        multiple times (`n_draws`) from each trained model's approximate posterior,
        and returns the mean of those samples.

        Parameters
        ----------
        transform_batch : int, default=0
            The batch index to condition on (i.e., as if all cells belonged to
            this batch).
        n_draws : int, default=25
            Number of forward passes (draws) to sample px for each model. The
            final px mean is averaged over these samples.

        Returns
        -------
        torch.Tensor
            A 2D tensor of shape (n_cells, n_genes) containing the average
            (across models and draws) of the px distribution means for each cell.

        """
        cont_obsm_key = "_scvi_extra_continuous_covs"
        n_cells = self.adata.n_obs
        x_ = (
            torch.tensor(self.adata.X.toarray(), dtype=torch.float32)
            if hasattr(self.adata.X, "toarray")
            else torch.tensor(self.adata.X, dtype=torch.float32)
        )
        batch_index = torch.full((n_cells, 1), transform_batch, dtype=torch.int64)

        if hasattr(self.adata.obsm[cont_obsm_key], "to_numpy"):
            cont_covs = torch.tensor(
                self.adata.obsm[cont_obsm_key].to_numpy(),
                dtype=torch.float32,
            )
        else:
            cont_covs = torch.tensor(
                self.adata.obsm[cont_obsm_key],
                dtype=torch.float32,
            )

        _px_mean_all: list[torch.Tensor] = []
        for model in tqdm(self.trained_models):
            if model.module is None:
                raise ValueError("Model is none. Please execute the training process.")
            with torch.no_grad():
                px_means_sample: list[torch.Tensor] = []
                for _ in tqdm(
                    range(n_draws),
                    leave=True,
                    desc="sampling px distribution",
                ):
                    inf_out = model.module.inference(
                        x=x_,
                        batch_index=batch_index,
                        cont_covs=cont_covs,
                        cat_covs=None,
                    )
                    gen_out = model.module.generative(
                        z=inf_out["z"],
                        library=inf_out["library"],
                        batch_index=torch.full(
                            (n_cells, 1),
                            transform_batch,
                            dtype=torch.int64,
                        ),
                        cont_covs=cont_covs,
                        cat_covs=None,
                    )
                    px_data: ZeroInflatedNegativeBinomial = gen_out["px"]
                    px_means_sample.append(px_data.mean)

            px_mean = torch.stack(px_means_sample, dim=-1).mean(dim=-1)
            _px_mean_all.append(px_mean)
        return torch.stack(_px_mean_all, dim=-1).mean(dim=-1)

    def regression(
        self,
        transform_batch: int = 0,
        stabilize_log1p: bool = True,
        n_draws: int = 25,
        mode: str = "ols",
    ) -> pd.DataFrame:
        """Perform regression of gene expression against the continuous covariate.

        Supported modes:
        - "ols":   Ordinary least squares (linear) regression. (Default)
                    Model: Y = β0 + β1 * X
        - "poly2": Quadratic regression (second-degree polynomial).
                    Model: Y = β0 + β1 * X + β2 * X^2
        - "spline": Cubic spline regression using patsy and statsmodels to capture
                    potentially more complex non-linear trends.
                    Model: Y = spline(X)  (with user-defined degrees of freedom, etc.)

        Parameters
        ----------
        transform_batch : int, default=0
            The batch index to condition on when sampling px.
        stabilize_log1p : bool, default=True
            Whether to apply log1p to the sampled expression values before regression.
        n_draws : int, default=25
            Number of forward passes (draws) to sample px from each model. The
            expression mean is averaged over these draws.
        mode : str, default="ols"
            The regression mode. Choose from:
            - "ols"
            - "poly2"
            - "spline"

        Returns
        -------
        pd.DataFrame
            A DataFrame with per-gene regression results. The columns depend on the
            specified mode:

            If mode="ols", columns are:
                "gene", "slope", "intercept", "r2"
            If mode="poly2", columns are:
                "gene", "coef_x2", "coef_x1", "intercept", "r2"
            If mode="spline", columns are:
                "gene", "coef_bs0", "coef_bs1", ..., "coef_bsn", "r2"
            (where n depends on the number of spline basis terms).
            The rows are sorted by the primary linear coefficient in the linear
            or poly2 modes, and left unsorted in spline mode (since multiple basis
            coefficients exist).

        Raises
        ------
        ValueError
            If `self.continuous_key` is None or if `mode` is not recognized.

        Examples
        --------
        >>> # Default OLS mode
        >>> df_ols = trained_vi.regression()
        >>> # Quadratic regression
        >>> df_poly = trained_vi.regression(mode="poly2")
        >>> # Cubic spline regression
        >>> df_spline = trained_vi.regression(mode="spline")

        """
        if self.continuous_key is None:
            raise ValueError("continuous_key must not be None in regression")

        if mode not in ("ols", "poly2", "spline"):
            raise ValueError(
                "Unsupported mode. Choose from ['ols', 'poly2', 'spline']."
            )

        # Copy the AnnData and extract the continuous variable
        _adata = self.adata.copy()
        _cont_vector = _adata.obs[self.continuous_key].astype(float).to_numpy()

        # Sample px from the models
        _px = self.sample_px(transform_batch=transform_batch, n_draws=n_draws)
        px_mean: np.ndarray = (
            np.log1p(_px.cpu().numpy()) if stabilize_log1p else _px.cpu().numpy()
        )

        if mode == "ols":
            # Prepare containers for OLS results
            _slope_all = np.zeros((_adata.n_vars), dtype=np.float32)
            _intercept_all = np.zeros((_adata.n_vars), dtype=np.float32)
            _r2_all = np.zeros((_adata.n_vars), dtype=np.float32)

            for g_idx in tqdm(
                range(_adata.n_vars), leave=True, desc="OLS regression for each gene"
            ):
                y_ = px_mean[:, g_idx]
                x_ = sm.add_constant(_cont_vector)
                model_ols = sm.OLS(y_, x_).fit()

                _slope_all[g_idx] = model_ols.params[1]
                _intercept_all[g_idx] = model_ols.params[0]
                _r2_all[g_idx] = model_ols.rsquared

            df_result = pd.DataFrame({
                "gene": _adata.var_names.to_numpy(),
                "slope": _slope_all,
                "intercept": _intercept_all,
                "r2": _r2_all,
            }).sort_values("slope", ascending=False)

        elif mode == "poly2":
            # Prepare containers for second-degree polynomial results
            _coef_x2_all = np.zeros((_adata.n_vars), dtype=np.float32)
            _coef_x1_all = np.zeros((_adata.n_vars), dtype=np.float32)
            _intercept_all = np.zeros((_adata.n_vars), dtype=np.float32)
            _r2_all = np.zeros((_adata.n_vars), dtype=np.float32)

            for g_idx in tqdm(
                range(_adata.n_vars), leave=True, desc="Poly2 regression for each gene"
            ):
                y_ = px_mean[:, g_idx]
                x_ = _cont_vector
                # Design matrix for [x^2, x, 1]
                X_poly = np.column_stack([x_**2, x_, np.ones_like(x_)])
                model_poly = sm.OLS(y_, X_poly).fit()

                _coef_x2_all[g_idx] = model_poly.params[0]
                _coef_x1_all[g_idx] = model_poly.params[1]
                _intercept_all[g_idx] = model_poly.params[2]
                _r2_all[g_idx] = model_poly.rsquared

            df_result = pd.DataFrame({
                "gene": _adata.var_names.to_numpy(),
                "coef_x2": _coef_x2_all,
                "coef_x1": _coef_x1_all,
                "intercept": _intercept_all,
                "r2": _r2_all,
            }).sort_values("coef_x1", ascending=False)

        else:  # mode == "spline"
            # We'll use patsy to create a cubic spline basis with df=5 (example)
            # You can adjust 'df' to control spline flexibility

            # First, let's figure out how many genes to store results for
            n_genes = _adata.n_vars

            # We'll do one pass to see how many columns (basis terms) are in the spline design
            # We include an intercept in the design by 'include_intercept=True', but
            # patsy also sometimes adds a column for that. We'll confirm after building X_spline.
            test_X_spline = patsy.dmatrix(
                "bs(x, df=5, degree=3, include_intercept=True)",
                {"x": _cont_vector},
                return_type="dataframe",
            )
            n_spline_cols = test_X_spline.shape[1]

            # Prepare arrays for storing coefficients
            coef_arrays = {
                f"coef_bs{i}": np.zeros(n_genes, dtype=np.float32)
                for i in range(n_spline_cols)
            }
            _r2_all = np.zeros((n_genes,), dtype=np.float32)

            for g_idx in tqdm(
                range(n_genes), leave=True, desc="Spline regression for each gene"
            ):
                y_ = px_mean[:, g_idx]
                # Build the spline design matrix for this batch of x-values
                X_spline = patsy.dmatrix(
                    "bs(x, df=5, degree=3, include_intercept=True)",
                    {"x": _cont_vector},
                    return_type="dataframe",
                )
                model_spline = sm.OLS(y_, X_spline).fit()
                _r2_all[g_idx] = model_spline.rsquared

                # Store each basis coefficient in the respective array
                for i, col in enumerate(X_spline.columns):
                    coef_arrays[f"coef_bs{i}"][g_idx] = model_spline.params[col]

            # Build the final DataFrame
            data_dict = {
                "gene": _adata.var_names.to_numpy(),
                "r2": _r2_all,
            }
            # Add the spline coefficients to data_dict
            data_dict.update(coef_arrays)
            df_result = pd.DataFrame(data_dict)

            # For splines, there's no single slope to sort by
            # so we can leave it unsorted or pick a basis coefficient to sort.
            # We'll leave it unsorted here.

        return df_result

    def regress_advanced(
        self,
        transform_batch: int = 0,
        stabilize_log1p: bool = True,
        mode: Literal["ols", "poly2", "spline"] = "ols",
        n_samples: int = 1,
        batch_size: int = 512,
        spline_df: int = 5,
        spline_degree: int = 3,
        n_threads: Optional[int] = None,
    ) -> pd.DataFrame:
        """Perform gene-wise regression of scVI-imputed expression values (px) against a continuous covariate,
        optionally sampling the latent variable z multiple times per cell to estimate parameter uncertainty.
        The final regression (OLS) step can be executed in parallel via multithreading.

        Parameters
        ----------
        transform_batch : int, optional
            Batch index to which all cells are 'transformed' when generating px.
            Use this to remove batch effects consistently.
        stabilize_log1p : bool, optional
            If True (default), applies log1p to the px values before regression.
        mode : {"ols", "poly2", "spline"}, optional
            Regression model. Choose:
            - "ols":   Linear regression (Y = β0 + β1 * X).
            - "poly2": Quadratic regression (Y = β0 + β1 * X + β2 * X^2).
            - "spline": Spline regression using patsy (e.g., cubic splines).
        n_samples : int, optional
            Number of times to sample z for each cell. If 1, we effectively get
            a single pass (point estimate). If >1, multiple passes are aggregated
            into a distribution of regression parameters.
        batch_size : int, optional
            Mini-batch size for sampling latent variables, useful for large datasets.
        spline_df : int, optional
            Degrees of freedom for spline basis if mode="spline". Passed to patsy.bs(..., df=spline_df).
        spline_degree : int, optional
            Polynomial degree for the spline if mode="spline". Passed to patsy.bs(..., degree=spline_degree).
        n_threads : int or None, optional
            Number of threads to use for parallelizing the gene-wise regressions. If None,
            defaults to the system's available resources.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing per-gene regression parameter statistics. Columns include:
            - For OLS: "Intercept_..." and "Slope_..." summary columns
            - For poly2: "Coef_x2_...", "Coef_x1_...", "Intercept_..." columns
            - For spline: one column per spline basis, e.g. "bs(x, df=...)[0]_..." etc.
            Also includes "r2_mean", "r2_std", "r2_2.5pct", "r2_97.5pct", "r2_prob_positive"
            summarizing R^2 across samples. If n_samples=1, std, percentile, and prob_positive
            are still present but reflect a single-sample distribution.

        Notes
        -----
        - This code assumes:
            * self.adata : AnnData
            * self.trained_models : List of scVI models
            * self.continuous_key : str (the .obs key for the continuous covariate)
        - The sampling is done using only the first model in self.trained_models.
        - The actual speedup may depend on your Python environment, since StatsModels is
        partly Python-based and the GIL may affect performance. However, for I/O or
        native-extension-bound tasks, this can still provide benefits.

        """
        # -----------------------------------------------------------------------
        # 1) Basic validations and data extraction
        # -----------------------------------------------------------------------
        if self.continuous_key is None:
            raise ValueError("continuous_key must not be None for regression.")

        if mode not in {"ols", "poly2", "spline"}:
            raise ValueError("Unsupported mode. Use 'ols', 'poly2', or 'spline'.")

        adata_local = self.adata.copy()
        continuous_values = (
            adata_local.obs[self.continuous_key].astype(float).to_numpy()
        )
        n_cells = adata_local.n_obs
        n_genes = adata_local.n_vars
        gene_names = adata_local.var_names.to_numpy()

        # -----------------------------------------------------------------------
        # 2) Helper functions: inside the main function
        # -----------------------------------------------------------------------

        def sample_px_multiple_z(n_samp: int) -> np.ndarray:
            """Sample the latent variable z for each cell n_samp times, then decode to px.
            Returns a NumPy array of shape (n_samp, n_cells, n_genes).
            """
            px_array = np.zeros((n_samp, n_cells, n_genes), dtype=np.float32)
            cont_obsm_key = "_scvi_extra_continuous_covs"
            all_indices = np.arange(n_cells)

            # We'll use the first model in self.trained_models
            model_module = self.trained_models[0].module
            if model_module is None:
                raise ValueError(
                    "Model module is None; ensure the model is trained/loaded correctly."
                )

            # Mini-batch iteration
            for start_idx in tqdm(
                range(0, n_cells, batch_size), desc="Sampling px", leave=True
            ):
                end_idx = min(start_idx + batch_size, n_cells)
                idx_batch = all_indices[start_idx:end_idx]

                x_batch = adata_local.X[idx_batch]
                if hasattr(x_batch, "toarray"):
                    x_batch = x_batch.toarray()
                x_batch_torch = torch.tensor(x_batch, dtype=torch.float32)

                batch_idx_torch = torch.full(
                    (len(idx_batch), 1), transform_batch, dtype=torch.int64
                )

                # Extra continuous covariates (e.g., pseudotime) for the decoder
                cont_covs_batch = (
                    adata_local.obsm[cont_obsm_key].iloc[idx_batch].to_numpy()
                )
                cont_covs_batch_torch = torch.tensor(
                    cont_covs_batch, dtype=torch.float32
                )

                # Sample n_samp times
                for s_i in range(n_samp):
                    with torch.no_grad():
                        # Inference pass to sample z
                        inference_out = model_module.inference(
                            x=x_batch_torch,
                            batch_index=batch_idx_torch,
                            cont_covs=cont_covs_batch_torch,
                            cat_covs=None,
                            n_samples=1,
                        )
                        # Generative pass to obtain px
                        generative_out = model_module.generative(
                            z=inference_out["z"],
                            library=inference_out["library"],
                            batch_index=batch_idx_torch,
                            cont_covs=cont_covs_batch_torch,
                            cat_covs=None,
                        )
                    px_data: ZeroInflatedNegativeBinomial = generative_out[
                        "px"
                    ]  # ZeroInflatedNegativeBinomial or NB
                    px_array[s_i, idx_batch, :] = px_data.mean.cpu().numpy()

            return px_array

        def compute_stats(array_2d: np.ndarray) -> dict:
            """Given array_2d of shape (n_samples, n_genes).

            compute:
            - mean
            - std
            - 2.5 percentile
            - 97.5 percentile
            - prob_positive (fraction of samples > 0)

            Returns a dict with these keys:
            ["mean", "std", "2.5pct", "97.5pct", "prob_positive"].
            """
            mean_ = array_2d.mean(axis=0)
            std_ = array_2d.std(axis=0)
            pct2_5 = np.percentile(array_2d, 2.5, axis=0)
            pct97_5 = np.percentile(array_2d, 97.5, axis=0)
            prob_pos = (array_2d > 0).mean(axis=0)

            return {
                "mean": mean_,
                "std": std_,
                "2.5pct": pct2_5,
                "97.5pct": pct97_5,
                "prob_positive": prob_pos,
            }

        # -----------------------------------------------------------------------
        # 3) Sample px from the latent space (n_samples times if requested)
        # -----------------------------------------------------------------------
        px_samples = sample_px_multiple_z(n_samples)
        # Optionally apply log1p
        if stabilize_log1p:
            px_samples = np.log1p(px_samples)

        # -----------------------------------------------------------------------
        # 4) Construct the design matrix for the chosen regression mode
        # -----------------------------------------------------------------------
        if mode == "ols":
            X_design = sm.add_constant(continuous_values)  # shape=(n_cells,2)
            design_cols = ["Intercept", "Slope"]
        elif mode == "poly2":
            X_design = np.column_stack([
                continuous_values**2,
                continuous_values,
                np.ones_like(continuous_values),
            ])
            design_cols = ["Coef_x2", "Coef_x1", "Intercept"]
        else:  # "spline"
            spline_frame = patsy.dmatrix(
                f"bs(x, df={spline_df}, degree={spline_degree}, include_intercept=True)",
                {"x": continuous_values},
                return_type="dataframe",
            )
            X_design = spline_frame.to_numpy()
            design_cols = list(spline_frame.columns)

        n_params = X_design.shape[1]

        # -----------------------------------------------------------------------
        # 5) Parallelized regression over all samples and genes
        #
        #    We'll create one task per (sample_index, gene_index). Then we use
        #    ThreadPoolExecutor to run them concurrently. tqdm will track the
        #    completion of all tasks.
        # -----------------------------------------------------------------------

        # Prepare arrays to hold results
        param_values = np.zeros((n_samples, n_genes, n_params), dtype=np.float32)
        r2_values = np.zeros((n_samples, n_genes), dtype=np.float32)

        def _fit_one_gene(task: tuple, x_mat: np.ndarray) -> tuple:
            """Helper function to fit a single gene's data to OLS.

            task: (s_index, gene_index, y_values)
            x_mat: design matrix shared by all
            """
            s_idx, g_idx, y_ = task
            reg_res = sm.OLS(y_, x_mat).fit()
            return s_idx, g_idx, reg_res.params, reg_res.rsquared

        # Build the tasks
        tasks = []
        for s_idx in range(n_samples):
            current_px = px_samples[s_idx]  # (n_cells, n_genes)
            for g_idx in range(n_genes):
                y_vals = current_px[:, g_idx]
                tasks.append((s_idx, g_idx, y_vals))

        # Run in multithreaded mode
        with ThreadPoolExecutor(max_workers=n_threads) as executor:
            future_list = [executor.submit(_fit_one_gene, t, X_design) for t in tasks]
            desc_msg = "Fitting regressions (threads)"
            for future in tqdm(
                as_completed(future_list),
                total=len(future_list),
                desc=desc_msg,
                leave=True,
            ):
                s_idx, g_idx, params, r2_val = future.result()
                param_values[s_idx, g_idx, :] = params
                r2_values[s_idx, g_idx] = r2_val

        # -----------------------------------------------------------------------
        # 6) Compute summary statistics across n_samples for each parameter & r2
        # -----------------------------------------------------------------------
        parameters_summary = {}
        for param_idx, col_name in enumerate(design_cols):
            param_array = param_values[:, :, param_idx]  # shape=(n_samples, n_genes)
            parameters_summary[col_name] = compute_stats(param_array)

        r2_summary = compute_stats(r2_values)

        # -----------------------------------------------------------------------
        # 7) Build the final DataFrame with summarized stats
        # -----------------------------------------------------------------------
        output_dict = {"gene": gene_names}

        # Parameter columns
        for col_name, stats_dict in parameters_summary.items():
            output_dict[f"{col_name}_mean"] = stats_dict["mean"]
            output_dict[f"{col_name}_std"] = stats_dict["std"]
            output_dict[f"{col_name}_2.5pct"] = stats_dict["2.5pct"]
            output_dict[f"{col_name}_97.5pct"] = stats_dict["97.5pct"]
            output_dict[f"{col_name}_prob_positive"] = stats_dict["prob_positive"]

        # R^2 columns
        output_dict["r2_mean"] = r2_summary["mean"]
        output_dict["r2_std"] = r2_summary["std"]
        output_dict["r2_2.5pct"] = r2_summary["2.5pct"]
        output_dict["r2_97.5pct"] = r2_summary["97.5pct"]
        output_dict["r2_prob_positive"] = r2_summary["prob_positive"]

        regression_output = pd.DataFrame(output_dict)

        # -----------------------------------------------------------------------
        # 8) Optional: sort by a main coefficient, depending on the mode
        # -----------------------------------------------------------------------
        if mode == "ols" and "Slope_mean" in regression_output.columns:
            regression_output = regression_output.sort_values(
                "Slope_mean", ascending=False
            )
        elif mode == "poly2" and "Coef_x1_mean" in regression_output.columns:
            regression_output = regression_output.sort_values(
                "Coef_x1_mean", ascending=False
            )
        # for spline, we do not apply any default sorting

        return regression_output.reset_index(drop=True)

    class Embeddings:
        """Embeddings class for handling dimensional reductions and plotting.

        An instance of this class is created after calling `calc_embeddings()`
        on the parent `TrainedContinuousVI` object. Provides convenience methods
        for plotting UMAP or other embeddings with gene or metadata coloring.
        """

        def __init__(self, trained_vi: TrainedContinuousVI) -> None:
            """Construct an Embeddings object.

            Parameters
            ----------
            trained_vi : TrainedContinuousVI
                The parent TrainedContinuousVI instance containing the AnnData
                and trained models.

            """
            self.trained_vi = trained_vi

        def umap(
            self,
            color_by: list[str] | None = None,
            n_draw: int = 25,
            transform_batch: int | str | None = None,
            n_use_model: int = 0,
        ) -> TrainedContinuousVI.Embeddings:
            """Plot a UMAP embedding colored by genes or metadata.

            If `color_by` contains gene names that exist in `adata.var_names`,
            expression levels are sampled from the scVI models. If `color_by`
            contains column names that exist in `adata.obs`, those columns are used
            for coloring. The resulting AnnData (with X_umap, X_latent, etc.)
            is then plotted via `scanpy.pl.umap`.

            Parameters
            ----------
            color_by : list of str, optional
                A list of gene names (in `adata.var_names`) or column names (in `adata.obs`)
                by which to color the UMAP plot.
            n_draw : int, default=25
                Number of forward passes (draws) to estimate gene expression with scVI
                for coloring genes. Ignored for categorical obs coloring.
            transform_batch : int, str, or None, default=None
                The batch to condition on when estimating normalized gene expression.
                If None, no specific batch transformation is applied.
            n_use_model : int, default=0
                The index of the trained model to use when obtaining latent coordinates
                (if needed).

            Returns
            -------
            TrainedContinuousVI.Embeddings
                The Embeddings instance (self) for potential chaining.

            """
            unique_color_by: list[str] | None = (
                list(dict.fromkeys(color_by)) if color_by is not None else None
            )
            _target_vars: list[str] = []
            _target_obs: list[str] = []

            if unique_color_by is not None:
                for c in unique_color_by:
                    if c in self.trained_vi.adata.var_names:
                        _target_vars.append(c)
                    elif c in self.trained_vi.adata.obs.columns:
                        _target_obs.append(c)

                expression: np.ndarray | None = None
                if len(_target_vars) > 0:
                    expression = np.mean(
                        [
                            model.get_normalized_expression(
                                self.trained_vi.adata,
                                gene_list=_target_vars,
                                n_samples=n_draw,
                                transform_batch=transform_batch,
                            )
                            for model in tqdm(
                                self.trained_vi.trained_models,
                                desc="Sampling expression",
                                leave=True,
                            )
                        ],
                        axis=0,
                    )

                obs_df: pd.DataFrame = (
                    self.trained_vi.adata.obs[_target_obs]
                    if len(_target_obs) > 0
                    else pd.DataFrame(index=self.trained_vi.adata.obs.index)
                )
                vars_df: pd.DataFrame | None = None
                if len(_target_vars) > 0:
                    vars_df = self.trained_vi.adata.var[
                        self.trained_vi.adata.var.index.isin(_target_vars)
                    ]

                _adata = sc.AnnData(
                    X=expression,
                    obs=obs_df,
                    var=vars_df,
                    obsm={
                        "X_latent": self.trained_vi.latent_coord(n_use_model),
                        "X_umap": self.trained_vi.adata.obsm["X_umap"],
                    },
                )
            if color_by is not None:
                sc.pl.umap(_adata, color=color_by)
            else:
                sc.pl.umap(_adata)

            return self
