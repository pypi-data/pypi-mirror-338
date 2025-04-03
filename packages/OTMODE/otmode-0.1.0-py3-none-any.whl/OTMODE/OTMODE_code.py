import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ot
from scipy.stats import gaussian_kde
from sklearn.decomposition import PCA
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scanpy as sc
import anndata as ad
from scipy.stats import norm
from statsmodels.stats.multitest import multipletests
import warnings
# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')



def filter_genes_expressed_in_both_groups(
    adata: ad.AnnData,
    group_column: str,
    group1: str,
    group2: str,
    threshold: int = 5
) -> ad.AnnData:
    """
    Filters genes in an AnnData object to keep only those expressed in both specified groups.

    Parameters:
    - adata (AnnData): The input AnnData object.
    - group_column (str): Column name in `.obs` that contains group labels.
    - group1 (str): Name of the first group (e.g., 'aHD').
    - group2 (str): Name of the second group (e.g., 'aSLE').
    - threshold (int): Minimum number of cells a gene must be expressed in (>0) to be considered expressed.

    Returns:
    - AnnData: A new AnnData object filtered to keep only genes expressed in both groups.
    """
    # Create masks for each group
    group1_mask = np.sum(adata[adata.obs[group_column] == group1].X > 0, axis=0) > threshold
    group2_mask = np.sum(adata[adata.obs[group_column] == group2].X > 0, axis=0) > threshold

    # Find genes expressed in both groups
    expressed_in_both = np.array(group1_mask).ravel() & np.array(group2_mask).ravel()

    # Return filtered AnnData object
    return adata[:, expressed_in_both].copy()



def extract_group_expression(
    adata: ad.AnnData,
    group_column: str,
    group_labels: list
) -> pd.DataFrame:
    """
    Extracts gene expression data for specified groups and returns a DataFrame.

    Parameters:
    - adata (AnnData): Filtered AnnData object.
    - group_column (str): Column in `.obs` that contains group labels.
    - group_labels (list): List of group names to include (e.g., ['cHD', 'aHD']).

    Returns:
    - pd.DataFrame: Gene expression matrix with genes as columns.
    """
    group_data = adata[adata.obs[group_column].isin(group_labels)]
    genes = adata.var_names

    # Convert sparse matrix to dense if needed
    if hasattr(group_data.X, "toarray"):
        expression = group_data.X.toarray()
    else:
        expression = group_data.X

    return pd.DataFrame(expression, columns=genes)


def perform_pca(
    expression_df: pd.DataFrame,
    n_components: int = 15
) -> np.ndarray:
    """
    Performs PCA on the expression DataFrame.

    Parameters:
    - expression_df (pd.DataFrame): Gene expression matrix.
    - n_components (int): Number of PCA components to compute.

    Returns:
    - np.ndarray: Transformed PCA components.
    """
    pca = PCA(n_components=n_components)
    pcs = pca.fit_transform(expression_df)
    return pcs



def fit_kde(pcs: np.ndarray, bw_method: str = 'scott') -> gaussian_kde:
    """
    Fits a Gaussian KDE to the input principal components.

    Parameters:
    - pcs (np.ndarray): PCA-transformed data (rows = samples, cols = components).
    - bw_method (str): Bandwidth estimation method (default: 'scott').

    Returns:
    - gaussian_kde: Fitted KDE object.
    """
    return gaussian_kde(pcs.T, bw_method=bw_method)



def evaluate_density(kde_model: gaussian_kde, pcs: np.ndarray) -> np.ndarray:
    """
    Evaluates density values for the input PCA data using a fitted KDE model.

    Parameters:
    - kde_model (gaussian_kde): Fitted KDE model.
    - pcs (np.ndarray): PCA-transformed data.

    Returns:
    - np.ndarray: Density estimates.
    """
    return kde_model(pcs.T)



def normalize_density(density: np.ndarray) -> np.ndarray:
    """
    Normalizes a density array using min-max scaling to [0, 1].

    Parameters:
    - density (np.ndarray): Raw density values.

    Returns:
    - np.ndarray: Normalized density values (between 0 and 1).
    """
    min_val = np.min(density)
    max_val = np.max(density)
    if max_val - min_val == 0:
        return np.zeros_like(density)
    return (density - min_val) / (max_val - min_val)



def compute_cost_matrix(
    X1: np.ndarray,
    X2: np.ndarray,
    metric: str = 'euclidean'
) -> np.ndarray:
    """
    Computes the cost matrix (pairwise distances) between two sets of samples.

    Parameters:
    - X1 (np.ndarray): Samples from group 1 (shape: [n_samples_1, n_features]).
    - X2 (np.ndarray): Samples from group 2 (shape: [n_samples_2, n_features]).
    - metric (str): Distance metric to use (default: 'euclidean').

    Returns:
    - np.ndarray: Cost matrix of shape [n_samples_1, n_samples_2].
    """
    return ot.dist(X1, X2, metric=metric)



def normalize_cost_matrix(cost_matrix: np.ndarray) -> np.ndarray:
    """
    Normalizes a cost matrix using min-max scaling to [0, 1].

    Parameters:
    - cost_matrix (np.ndarray): Raw cost matrix.

    Returns:
    - np.ndarray: Normalized cost matrix.
    """
    min_val = np.min(cost_matrix)
    max_val = np.max(cost_matrix)
    if max_val - min_val == 0:
        return np.zeros_like(cost_matrix)
    return (cost_matrix - min_val) / (max_val - min_val)



def compute_transport_plan(
    mu: np.ndarray,
    nu: np.ndarray,
    cost_matrix: np.ndarray,
    reg: float = 1.0
) -> np.ndarray:
    """
    Computes the optimal transport plan using the Sinkhorn algorithm.

    Parameters:
    - mu (np.ndarray): Source distribution (must sum to 1).
    - nu (np.ndarray): Target distribution (must sum to 1).
    - cost_matrix (np.ndarray): Normalized cost matrix (shape: [n, m]).
    - reg (float): Regularization parameter (lambda).

    Returns:
    - np.ndarray: Optimal transport plan (same shape as cost_matrix).
    """

    # Run Sinkhorn algorithm
    transport_plan = ot.sinkhorn(mu, nu, cost_matrix, reg)
    return transport_plan



def compute_expression_difference(
    transport_plan: np.ndarray,
    source_expression: np.ndarray,
    target_expression: np.ndarray
) -> np.ndarray:
    """
    Computes gene expression differences between original and transported profiles.

    Parameters:
    - transport_plan (np.ndarray): Optimal transport plan (shape: [n_source, n_target]).
    - source_expression (np.ndarray): Expression matrix for source group (Group 0), shape [n_source, n_genes].
    - target_expression (np.ndarray): Expression matrix for target group (Group 1), shape [n_target, n_genes].

    Returns:
    - np.ndarray: Expression difference matrix, shape [n_source, n_genes].
    """
    # Normalize transport plan row-wise
    row_sums = transport_plan.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1  # Avoid division by zero
    transport_plan_normalized = transport_plan / row_sums

    # Compute transported expression profiles
    transported_expr = np.dot(transport_plan_normalized, target_expression)

    # Compute expression difference
    expr_difference = transported_expr - source_expression

    return expr_difference




def compute_standard_error(
    expr_diff: np.ndarray,
    ddof: int = 1
) -> np.ndarray:
    """
    Computes the standard error of expression differences for each gene.

    Parameters:
    - expr_diff (np.ndarray): Expression difference matrix [n_cells, n_genes].
    - ddof (int): Delta degrees of freedom for std calculation (default = 1).

    Returns:
    - np.ndarray: Adjusted standard error for each gene (shape: [n_genes]).
    """
    n_cells = expr_diff.shape[0]
    
    # Compute standard deviation across cells (per gene)
    std_diff = np.std(expr_diff, axis=0, ddof=ddof)
    
    # Compute standard error
    se_diff = std_diff / np.sqrt(n_cells)
    
    # Adjust to avoid division by zero
    se_diff_adj = np.where(se_diff == 0, np.finfo(float).eps, se_diff)

    return se_diff_adj



def perform_wald_test(
    expr_diff: np.ndarray,
    se_diff_adj: np.ndarray
) -> dict:
    """
    Performs Wald test on gene expression differences and applies FDR correction.

    Parameters:
    - expr_diff (np.ndarray): Expression difference matrix [n_cells, n_genes].
    - se_diff_adj (np.ndarray): Adjusted standard errors [n_genes].

    Returns:
    - dict: Dictionary with keys:
        - 'mean_diff': Mean expression difference per gene
        - 'wald_stat': Wald statistics per gene
        - 'p_values': Two-tailed p-values
        - 'adj_p_values': FDR-adjusted p-values (Benjamini-Hochberg)
    """
    # Compute mean difference
    mean_diff = np.mean(expr_diff, axis=0)

    # Compute Wald statistics
    wald_stat = mean_diff / se_diff_adj

    # Compute two-tailed p-values
    p_values = 2 * norm.sf(np.abs(wald_stat))

    # Adjust p-values using Benjamini-Hochberg FDR
    _, adj_p_values, _, _ = multipletests(p_values, method='fdr_bh')

    return {
        "mean_diff": mean_diff,
        "wald_stat": wald_stat,
        "p_values": p_values,
        "adj_p_values": adj_p_values
    }



def plot_pvalue_histogram(
    p_values: np.ndarray,
    bins: int = 50,
    title: str = "Histogram of P-Values under Null Hypothesis",
    figsize: tuple = (8, 6),
    color: str = 'skyblue'
):
    """
    Plots a histogram of p-values.

    Parameters:
    - p_values (np.ndarray): Array of p-values.
    - bins (int): Number of bins in the histogram (default: 50).
    - title (str): Plot title.
    - figsize (tuple): Size of the figure.
    - color (str): Bar color for the histogram.
    """
    plt.figure(figsize=figsize)
    plt.hist(p_values, bins=bins, color=color, edgecolor='black')
    plt.xlabel('P-Value')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()



def plot_gene_density_comparison(
    df_hd: pd.DataFrame,
    df_sle: pd.DataFrame,
    genes,
    group_labels: tuple = ("HD", "SLE"),
    figsize: tuple = (10, 6)
):
    """
    Plots KDE for one or more genes in both HD and SLE groups.

    Parameters:
    - df_hd (pd.DataFrame): Expression data for HD group.
    - df_sle (pd.DataFrame): Expression data for SLE group.
    - genes (str or list): One gene or list of genes to plot.
    - group_labels (tuple): Labels for the HD and SLE groups.
    - figsize (tuple): Size of each subplot.
    """
    if isinstance(genes, str):
        genes = [genes]  # Wrap single gene name in a list

    for gene in genes:
        if gene not in df_hd.columns or gene not in df_sle.columns:
            raise ValueError(f"Gene '{gene}' not found in one of the DataFrames.")

        plt.figure(figsize=figsize)
        sns.kdeplot(df_hd[gene], fill=True, label=group_labels[0], color='skyblue', linewidth=2)
        sns.kdeplot(df_sle[gene], fill=True, label=group_labels[1], color='salmon', linewidth=2)

        plt.xlabel('Expression Level')
        plt.ylabel('Density')
        plt.title(f"Density Comparison for Gene: {gene}")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.4)
        plt.tight_layout()
        plt.show()



def plot_gene_violin_comparison(
    df_hd: pd.DataFrame,
    df_sle: pd.DataFrame,
    genes,
    group_labels: tuple = ("HD", "SLE"),
    figsize: tuple = (8, 6)
):
    """
    Plots violin plots for one or more genes comparing HD vs SLE.

    Parameters:
    - df_hd (pd.DataFrame): Expression data for HD group.
    - df_sle (pd.DataFrame): Expression data for SLE group.
    - genes (str or list): One gene or list of genes to plot.
    - group_labels (tuple): Labels for HD and SLE groups.
    - figsize (tuple): Size of each individual figure.
    """
    if isinstance(genes, str):
        genes = [genes]

    for gene in genes:
        if gene not in df_hd.columns or gene not in df_sle.columns:
            raise ValueError(f"Gene '{gene}' not found in one of the DataFrames.")

        # Combine data
        df_plot = pd.DataFrame({
            "Expression": pd.concat([df_hd[gene], df_sle[gene]]),
            "Group": [group_labels[0]] * len(df_hd) + [group_labels[1]] * len(df_sle)
        })

        plt.figure(figsize=figsize)
        sns.violinplot(data=df_plot, x="Group", y="Expression", palette=["skyblue", "salmon"])
        plt.title(f"Violin Plot of {gene} Expression")
        plt.xlabel("Group")
        plt.ylabel("Expression Level")
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.show()



def plot_volcano_comparison(
    de_results_list,
    method_names,
    fc_col='Average_Expression_Diff',
    pval_col='AdjPValue',
    gene_count=10150,
    significance_level=0.05,
    figsize=(8, 7),
    titles=None
):
    """
    Plots multiple volcano plots side-by-side for differential expression results.

    Parameters:
    - de_results_list: List of DataFrames, each with fold change and adjusted p-value columns.
    - method_names: List of method names (used in legends and titles).
    - fc_col: Name of the column with fold change or avg expression difference.
    - pval_col: Name of the column with adjusted p-values.
    - gene_count: Total number of genes (used for Bonferroni correction).
    - significance_level: Base significance threshold (e.g., 0.05).
    - figsize: Tuple for figure size.
    - titles: List of titles for each subplot (optional).
    """
    num_methods = len(de_results_list)
    y_line = -np.log10(significance_level / gene_count)

    fig, axs = plt.subplots(1, num_methods, figsize=figsize, sharey=True)

    if num_methods == 1:
        axs = [axs]  # Ensure axs is always iterable

    for i, (df, method) in enumerate(zip(de_results_list, method_names)):
        ax = axs[i]
        ax.scatter(
            df[fc_col],
            -np.log10(df[pval_col]),
            alpha=0.3,
            label=method,
            color='steelblue'
        )
        ax.axhline(y=y_line, color='red', linestyle='--', linewidth=1)
        ax.set_xlabel('Average Expression Difference')
        if i == 0:
            ax.set_ylabel('-log10(Adjusted P-Value)')
        if titles:
            ax.set_title(titles[i])
        else:
            ax.set_title(f"{method} Method")
        ax.legend()

    plt.tight_layout()
    plt.show()



def plot_ot_sinkhorn_distances(
    df,
    x='Cell_Type_Prediction',
    y='Observed_OT_Distance',
    hue='Target_Cluster',
    figsize=(20, 8),
    title='OT Sinkhorn Distances per Cluster and Cell Type\nwith Bonferroni-Adjusted p-values',
    palette='tab20',
    save_path=None
):
    """
    Plots a bar chart of OT Sinkhorn distances grouped by predicted cell types and true clusters.

    Parameters:
    - df: pandas DataFrame containing the data
    - x: column name for x-axis (default: 'Cell_Type_Prediction')
    - y: column name for y-axis (default: 'Observed_OT_Distance')
    - hue: column name for grouping (default: 'Target_Cluster')
    - figsize: tuple for figure size (default: (20, 8))
    - title: plot title
    - palette: seaborn color palette (default: 'tab20')
    - save_path: if provided, saves the plot to the given file path
    """
    # Sort by OT distance within each cluster (optional for better visuals)
    df_sorted = (
        df.groupby(hue, group_keys=False)
        .apply(lambda x_: x_.sort_values(by=y, ascending=True))
    )

    # Create the plot
    plt.figure(figsize=figsize)
    sns.set(style="whitegrid")

    sns.barplot(
        data=df_sorted,
        x=x,
        y=y,
        hue=hue,
        palette=palette
    )

    plt.legend(title='True Cell Type Annotation', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('Predicted Cell Type Annotation', fontsize=12)
    plt.ylabel('Observed OT Sinkhorn Distance', fontsize=12)
    plt.title(title, fontsize=16)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()



# Define the assign_cell_types function as shown above
def assign_cell_types(df, adjusted_pval_col='Adjusted_p-value', pval_threshold=0):
    """
    Assigns cell types to target clusters based on the highest Observed_OT_Distance among significant associations.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the results with columns:
        ['Cell_Type_Prediction', 'Target_Cluster', 'Observed_OT_Distance', 'p-value', 'Adjusted_p-value']
    - adjusted_pval_col (str): Name of the column containing adjusted p-values.
    - pval_threshold (float): Threshold to determine significance (e.g., 0 for p <= 0).

    Returns:
    - cluster_to_celltype (dict): Mapping from Target_Cluster to Cell_Type_Prediction.
    - df_top_clusters (pd.DataFrame): DataFrame containing the top Target_Cluster for each Cell_Type_Prediction.
    """
    # Step 1: Filter for significant associations
    df_sig = df[df[adjusted_pval_col] <= pval_threshold].copy()

    # Ensure 'Observed_OT_Distance' is numeric
    df_sig['Observed_OT_Distance'] = pd.to_numeric(df_sig['Observed_OT_Distance'], errors='coerce')

    # Drop rows with missing Observed_OT_Distance
    df_sig = df_sig.dropna(subset=['Observed_OT_Distance'])

    # Step 2: For each Cell_Type_Prediction, find the Target_Cluster with the highest Observed_OT_Distance
    df_top_clusters = df_sig.loc[df_sig.groupby('Cell_Type_Prediction')['Observed_OT_Distance'].idxmax()].reset_index(drop=True)

    # Step 3: Create a mapping from Target_Cluster to Cell_Type_Prediction
    cluster_to_celltype = pd.Series(
        df_top_clusters.Cell_Type_Prediction.values,
        index=df_top_clusters.Target_Cluster
    ).to_dict()

    return cluster_to_celltype, df_top_clusters



def perform_annotation_analysis(marker_genes, adata, target_cluster, n_pc, num_permutations=1000, lambda_reg=10):
    """
    Perform OT Sinkhorn distance calculation and permutation test for a given set of marker genes.

    Parameters:
    - marker_genes: list of gene names to use for the analysis
    - adata: AnnData object containing your single-cell data
    - target_cluster: the cluster label (from 'louvain') to define group0
    - num_permutations: number of permutations for the permutation test
    - lambda_reg: regularization parameter for Sinkhorn

    Returns:
    - observed_distance: Observed OT Sinkhorn distance
    - p_value: p-value from the permutation test
    """
    # Set random seed for reproducibility
    np.random.seed(666)
    
    # Step 1: Define Group0 and Group1 based on target_cluster
    group0 = adata[adata.obs['leiden'] == target_cluster]
    group1 = adata[adata.obs['leiden'] != target_cluster]

    # Check if both groups have enough cells
    if group0.n_obs == 0 or group1.n_obs == 0:
        print(f"Insufficient cells in group0 or group1 for cluster {target_cluster}.")
        return np.nan, np.nan

    # Step 2: Extract gene expression data for the marker genes
    group0_marker = group0[:, marker_genes]
    group1_marker = group1[:, marker_genes]

    # Verify that marker genes are present
    if group0_marker.shape[1] == 0 or group1_marker.shape[1] == 0:
        print(f"No marker genes found for the provided list in cluster {target_cluster}. Skipping.")
        return np.nan, np.nan

    # Step 3: Convert to DataFrame for easier manipulation
    df_expression_group0 = pd.DataFrame(group0_marker.X.toarray(), columns=group0_marker.var_names)
    df_expression_group1 = pd.DataFrame(group1_marker.X.toarray(), columns=group1_marker.var_names)

    # Step 4: Perform PCA for dimensionality reduction
    pca = PCA(n_components=n_pc)
    group0_pcs = pca.fit_transform(df_expression_group0)
    group1_pcs = pca.fit_transform(df_expression_group1)  # Use transform to maintain PCA space

    # Step 5: Fit KDE for both groups in PCA space
    try:
        kde_group0 = stats.gaussian_kde(group0_pcs.T, bw_method='scott')
        kde_group1 = stats.gaussian_kde(group1_pcs.T, bw_method='scott')
    except np.linalg.LinAlgError:
        print(f"KDE failed for cluster {target_cluster}. Possibly due to singular data.")
        return np.nan, np.nan

    # Evaluate densities
    density_group0 = kde_group0(group0_pcs.T)
    density_group1 = kde_group1(group1_pcs.T)

    # Step 6: Normalize densities to create probability distributions
    mu = (density_group0 - density_group0.min()) / (density_group0.max() - density_group0.min())
    nu = (density_group1 - density_group1.min()) / (density_group1.max() - density_group1.min())

    # Step 7: Compute the cost matrix between cells in the two groups
    X_group0 = df_expression_group0.values
    X_group1 = df_expression_group1.values
    cost_matrix = ot.dist(X_group0, X_group1, metric='euclidean')
    cost_matrix_norm = (cost_matrix - cost_matrix.min()) / (cost_matrix.max() - cost_matrix.min())

    # Step 8: Compute the OT Sinkhorn plan and distance
    transport_plan = ot.sinkhorn(mu, nu, cost_matrix_norm, lambda_reg)
    observed_distance = np.sum(transport_plan * cost_matrix_norm)

    # Step 9: Permutation Test
    combined_X = np.vstack([X_group0, X_group1])
    n_group0 = X_group0.shape[0]
    n_group1 = X_group1.shape[0]
    permuted_distances = []

    for i in range(num_permutations):
        # Shuffle the combined data
        permuted_indices = np.random.permutation(combined_X.shape[0])
        perm_group0 = combined_X[permuted_indices[:n_group0], :]
        perm_group1 = combined_X[permuted_indices[n_group0:], :]

        # Perform PCA on permuted groups using the original PCA model
        try:
            perm_group0_pcs = pca.transform(perm_group0)
            perm_group1_pcs = pca.transform(perm_group1)
        except ValueError:
            # In case the permutation results in invalid data for PCA
            permuted_distances.append(np.nan)
            continue

        # Fit KDE for permuted groups
        try:
            kde_perm_group0 = stats.gaussian_kde(perm_group0_pcs.T, bw_method='scott')
            kde_perm_group1 = stats.gaussian_kde(perm_group1_pcs.T, bw_method='scott')
            # Evaluate densities
            density_perm_group0 = kde_perm_group0(perm_group0_pcs.T)
            density_perm_group1 = kde_perm_group1(perm_group1_pcs.T)
        except np.linalg.LinAlgError:
            # In case KDE fails due to singular data
            permuted_distances.append(np.nan)
            continue

        # Normalize densities
        mu_perm = (density_perm_group0 - density_perm_group0.min()) / (density_perm_group0.max() - density_perm_group0.min())
        nu_perm = (density_perm_group1 - density_perm_group1.min()) / (density_perm_group1.max() - density_perm_group1.min())

        # Compute cost matrix for permuted groups
        cost_matrix_perm = ot.dist(perm_group0, perm_group1, metric='euclidean')
        cost_matrix_perm_norm = (cost_matrix_perm - cost_matrix_perm.min()) / (cost_matrix_perm.max() - cost_matrix_perm.min())

        # Compute OT Sinkhorn distance for permuted data
        transport_plan_perm = ot.sinkhorn(mu_perm, nu_perm, cost_matrix_perm_norm, lambda_reg)
        ot_distance_perm = np.sum(transport_plan_perm * cost_matrix_perm_norm)
        permuted_distances.append(ot_distance_perm)

    # Remove NaN values resulting from failed permutations
    permuted_distances = np.array(permuted_distances)
    permuted_distances = permuted_distances[~np.isnan(permuted_distances)]

    # Calculate p-value
    if len(permuted_distances) == 0:
        p_value = np.nan
    else:
        p_value = np.mean(permuted_distances >= observed_distance)

    return observed_distance, p_value



# Define the assign_cell_types function as shown above
def assign_cell_types(df, adjusted_pval_col='Adjusted_p-value', pval_threshold=0):
    """
    Assigns cell types to target clusters based on the highest Observed_OT_Distance among significant associations.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the results with columns:
        ['Cell_Type_Prediction', 'Target_Cluster', 'Observed_OT_Distance', 'p-value', 'Adjusted_p-value']
    - adjusted_pval_col (str): Name of the column containing adjusted p-values.
    - pval_threshold (float): Threshold to determine significance (e.g., 0 for p <= 0).

    Returns:
    - cluster_to_celltype (dict): Mapping from Target_Cluster to Cell_Type_Prediction.
    - df_top_clusters (pd.DataFrame): DataFrame containing the top Target_Cluster for each Cell_Type_Prediction.
    """
    # Step 1: Filter for significant associations
    df_sig = df[df[adjusted_pval_col] <= pval_threshold].copy()

    # Ensure 'Observed_OT_Distance' is numeric
    df_sig['Observed_OT_Distance'] = pd.to_numeric(df_sig['Observed_OT_Distance'], errors='coerce')

    # Drop rows with missing Observed_OT_Distance
    df_sig = df_sig.dropna(subset=['Observed_OT_Distance'])

    # Step 2: For each Cell_Type_Prediction, find the Target_Cluster with the highest Observed_OT_Distance
    df_top_clusters = df_sig.loc[df_sig.groupby('Cell_Type_Prediction')['Observed_OT_Distance'].idxmax()].reset_index(drop=True)

    # Step 3: Create a mapping from Target_Cluster to Cell_Type_Prediction
    cluster_to_celltype = pd.Series(
        df_top_clusters.Cell_Type_Prediction.values,
        index=df_top_clusters.Target_Cluster
    ).to_dict()

    return cluster_to_celltype, df_top_clusters