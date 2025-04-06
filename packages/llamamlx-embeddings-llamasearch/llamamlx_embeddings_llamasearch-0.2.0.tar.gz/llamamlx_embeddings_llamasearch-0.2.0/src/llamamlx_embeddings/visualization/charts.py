"""
Visualization utilities for llamamlx-embeddings.
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

try:
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure

    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

try:
    import seaborn as sns

    SEABORN_AVAILABLE = True
except ImportError:
    SEABORN_AVAILABLE = False

try:
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE

    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

# Configure logging
logger = logging.getLogger(__name__)


def check_matplotlib():
    """Check if matplotlib is available and raise ImportError if not."""
    if not MATPLOTLIB_AVAILABLE:
        raise ImportError(
            "Matplotlib is required for visualization functions. "
            "Install it with 'pip install matplotlib'."
        )


def check_seaborn():
    """Check if seaborn is available and raise ImportError if not."""
    if not SEABORN_AVAILABLE:
        raise ImportError(
            "Seaborn is required for this visualization function. "
            "Install it with 'pip install seaborn'."
        )


def check_sklearn():
    """Check if scikit-learn is available and raise ImportError if not."""
    if not SKLEARN_AVAILABLE:
        raise ImportError(
            "Scikit-learn is required for dimensionality reduction. "
            "Install it with 'pip install scikit-learn'."
        )


def plot_benchmark_results(
    results: Union[Dict[str, Any], str, Path],
    metric: str = "throughput_texts_per_second",
    x_axis: str = "batch_size",
    group_by: Optional[str] = "text_length",
    title: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 6),
    save_path: Optional[Union[str, Path]] = None,
    dpi: int = 100,
    style: str = "default",
) -> Optional[Figure]:
    """
    Plot benchmark results with configurable options.

    Args:
        results: Benchmark results dictionary or path to JSON file
        metric: Name of the metric to plot
        x_axis: Name of the parameter to use as x-axis
        group_by: Optional parameter to group data by (will create multiple lines)
        title: Optional title for the plot
        figsize: Figure size as (width, height) in inches
        save_path: Optional path to save the figure
        dpi: DPI for the saved figure
        style: Plot style ('default', 'seaborn', etc.)

    Returns:
        Matplotlib Figure object if not saving, None if saving
    """
    check_matplotlib()

    # Set style if seaborn is available
    if style != "default" and SEABORN_AVAILABLE:
        sns.set_style(style)

    # Load results if a path is provided
    if isinstance(results, (str, Path)):
        with open(results, "r") as f:
            results = json.load(f)

    # Extract measurements
    measurements = results.get("measurements", [])
    if not measurements:
        logger.warning("No measurements found in benchmark results")
        return None

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Set title
    if title is None:
        model_id = results.get("model_id", "unknown")
        title = f"Benchmark Results for {model_id}"

    # Extract unique values for grouping
    if group_by is not None:
        group_values = sorted(set(m[group_by] for m in measurements if group_by in m))
    else:
        group_values = [None]

    # Plot data for each group
    for group_value in group_values:
        # Filter measurements for this group
        if group_by is not None:
            group_measurements = [m for m in measurements if m.get(group_by) == group_value]
            label = f"{group_by}={group_value}"
        else:
            group_measurements = measurements
            label = None

        # Sort by x-axis value
        group_measurements.sort(key=lambda m: m.get(x_axis, 0))

        # Extract x and y values
        x_values = [m.get(x_axis, 0) for m in group_measurements]
        y_values = [m.get(metric, 0) for m in group_measurements]

        # Plot line
        ax.plot(x_values, y_values, marker="o", label=label)

    # Add labels and legend
    ax.set_xlabel(x_axis.replace("_", " ").title())
    ax.set_ylabel(metric.replace("_", " ").title())
    ax.set_title(title)

    if group_by is not None:
        ax.legend()

    ax.grid(True, linestyle="--", alpha=0.7)

    # Save if requested
    if save_path is not None:
        plt.tight_layout()
        plt.savefig(save_path, dpi=dpi)
        plt.close(fig)
        logger.info(f"Saved benchmark plot to {save_path}")
        return None

    return fig


def visualize_similarity_matrix(
    similarity_matrix: np.ndarray,
    labels: Optional[List[str]] = None,
    title: str = "Similarity Matrix",
    figsize: Tuple[int, int] = (10, 8),
    cmap: str = "viridis",
    save_path: Optional[Union[str, Path]] = None,
    dpi: int = 100,
    annotate: bool = False,
) -> Optional[Figure]:
    """
    Visualize a similarity matrix as a heatmap.

    Args:
        similarity_matrix: Square matrix of similarity scores
        labels: Optional list of labels for items
        title: Title for the plot
        figsize: Figure size as (width, height) in inches
        cmap: Colormap to use
        save_path: Optional path to save the figure
        dpi: DPI for the saved figure
        annotate: Whether to annotate cells with values

    Returns:
        Matplotlib Figure object if not saving, None if saving
    """
    check_matplotlib()

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Plot heatmap
    im = ax.imshow(similarity_matrix, cmap=cmap)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("Similarity Score")

    # Set title
    ax.set_title(title)

    # Set labels if provided
    if labels is not None:
        # Ensure we have the right number of labels
        if len(labels) != similarity_matrix.shape[0]:
            logger.warning(
                f"Number of labels ({len(labels)}) doesn't match matrix dimensions "
                f"({similarity_matrix.shape[0]})"
            )
            labels = labels[: similarity_matrix.shape[0]]

        # Set tick labels
        ax.set_xticks(np.arange(len(labels)))
        ax.set_yticks(np.arange(len(labels)))
        ax.set_xticklabels(labels)
        ax.set_yticklabels(labels)

        # Rotate x-labels and set alignment
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Annotate cells with values if requested
    if annotate:
        for i in range(similarity_matrix.shape[0]):
            for j in range(similarity_matrix.shape[1]):
                text = ax.text(
                    j,
                    i,
                    f"{similarity_matrix[i, j]:.2f}",
                    ha="center",
                    va="center",
                    color="w" if similarity_matrix[i, j] < 0.7 else "black",
                )

    # Set aspect and layout
    ax.set_aspect("equal")
    fig.tight_layout()

    # Save if requested
    if save_path is not None:
        plt.savefig(save_path, dpi=dpi)
        plt.close(fig)
        logger.info(f"Saved similarity matrix visualization to {save_path}")
        return None

    return fig


def visualize_embeddings_2d(
    embeddings: List[np.ndarray],
    labels: Optional[List[str]] = None,
    method: str = "tsne",
    title: str = "Embedding Visualization",
    figsize: Tuple[int, int] = (10, 8),
    save_path: Optional[Union[str, Path]] = None,
    dpi: int = 100,
    random_state: int = 42,
    show_legend: bool = True,
) -> Optional[Figure]:
    """
    Visualize high-dimensional embeddings in 2D.

    Args:
        embeddings: List of embedding vectors
        labels: Optional list of labels or categories for coloring
        method: Dimensionality reduction method ('tsne' or 'pca')
        title: Title for the plot
        figsize: Figure size as (width, height) in inches
        save_path: Optional path to save the figure
        dpi: DPI for the saved figure
        random_state: Random seed for reproducibility
        show_legend: Whether to show the legend

    Returns:
        Matplotlib Figure object if not saving, None if saving
    """
    check_matplotlib()
    check_sklearn()

    # Convert list of embeddings to a single array
    embeddings_array = np.array(embeddings)

    # Apply dimensionality reduction
    if method.lower() == "tsne":
        reducer = TSNE(n_components=2, random_state=random_state)
        reduced_embeddings = reducer.fit_transform(embeddings_array)
    elif method.lower() == "pca":
        reducer = PCA(n_components=2, random_state=random_state)
        reduced_embeddings = reducer.fit_transform(embeddings_array)
    else:
        raise ValueError(f"Unknown dimensionality reduction method: {method}")

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Plot embeddings
    if labels is not None:
        # Get unique labels
        unique_labels = sorted(set(labels))

        # Create color map
        cmap = plt.cm.get_cmap("tab10", len(unique_labels))

        # Plot each category with a different color
        for i, label in enumerate(unique_labels):
            mask = [l == label for l in labels]
            ax.scatter(
                reduced_embeddings[mask, 0],
                reduced_embeddings[mask, 1],
                label=label,
                alpha=0.7,
                color=cmap(i),
            )

        if show_legend:
            ax.legend()
    else:
        ax.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], alpha=0.7)

    # Add title and labels
    ax.set_title(title)
    ax.set_xlabel(f"{method.upper()} Dimension 1")
    ax.set_ylabel(f"{method.upper()} Dimension 2")

    # Set layout
    fig.tight_layout()

    # Save if requested
    if save_path is not None:
        plt.savefig(save_path, dpi=dpi)
        plt.close(fig)
        logger.info(f"Saved embedding visualization to {save_path}")
        return None

    return fig
