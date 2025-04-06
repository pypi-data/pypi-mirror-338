"""
Sparse embedding implementation and utilities for llamamlx-embeddings.
"""

import math
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

# Import MLX components explicitly to avoid undefined references
import mlx.core as mx
import mlx.nn as nn
import numpy as np


@dataclass
class SparseEmbedding:
    """
    Represents a sparse embedding vector.
    Uses a dataclass for clarity and type safety.
    """

    indices: List[int]  # Indices of non-zero elements
    values: List[float]  # Corresponding values

    @classmethod
    def from_dense(cls, dense_vector: mx.array, threshold: float = 1e-6) -> "SparseEmbedding":
        """
        Creates a SparseEmbedding from a dense vector, applying a threshold.

        Args:
            dense_vector: The dense vector (mx.array)
            threshold: Values below this are considered zero

        Returns:
            A SparseEmbedding object
        """
        # Convert to numpy for easier manipulation, then back to lists
        dense_np = np.array(dense_vector)
        indices = np.nonzero(np.abs(dense_np) > threshold)[0].tolist()
        values = dense_np[indices].tolist()
        return cls(indices=indices, values=values)

    def to_dense(self, dimension: int) -> mx.array:
        """
        Converts the sparse embedding back to a dense vector.

        Args:
            dimension: The dimensionality of the dense vector

        Returns:
            The dense vector as an mx.array
        """
        dense = mx.zeros(dimension, dtype=mx.float32)
        if self.indices:  # Check if indices is not empty
            dense[mx.array(self.indices)] = mx.array(self.values)
        return dense

    def __len__(self) -> int:
        """Return the number of non-zero elements."""
        return len(self.indices)

    def __str__(self) -> str:
        """String representation for debugging."""
        if len(self.indices) > 5:
            # Show a truncated version if too many elements
            indices_str = str(self.indices[:5])[:-1] + ", ...]"
            values_str = str(self.values[:5])[:-1] + ", ...]"
        else:
            indices_str = str(self.indices)
            values_str = str(self.values)

        return f"SparseEmbedding(non_zeros={len(self.indices)}, indices={indices_str}, values={values_str})"


def sparse_dense_mm(sparse_matrix: List[SparseEmbedding], dense_matrix: mx.array) -> mx.array:
    """
    Performs a sparse-dense matrix multiplication. Optimized for MLX.

    Args:
        sparse_matrix: A list of SparseEmbedding objects (rows of the sparse matrix)
        dense_matrix: The dense matrix (mx.array)

    Returns:
        The result of the matrix multiplication (mx.array)
    """
    # This implementation uses explicit loops, optimized for MLX's lazy evaluation
    out_rows = []
    for sparse_row in sparse_matrix:
        if not sparse_row.indices:  # Handle empty sparse vectors
            # Add a row of zeros with the right shape
            out_rows.append(mx.zeros(dense_matrix.shape[1], dtype=dense_matrix.dtype))
            continue

        indices = mx.array(sparse_row.indices)
        values = mx.array(sparse_row.values)

        # Multiply the relevant columns of the dense matrix by the sparse values
        selected_cols = dense_matrix[indices]
        out_row = mx.sum(values.reshape(-1, 1) * selected_cols, axis=0)
        out_rows.append(out_row)

    return mx.stack(out_rows)


def sparse_normalize(sparse_embedding: SparseEmbedding) -> SparseEmbedding:
    """
    Normalizes a sparse embedding vector.

    Args:
        sparse_embedding: The SparseEmbedding to normalize

    Returns:
        The normalized SparseEmbedding
    """
    if not sparse_embedding.values:  # Handle empty sparse vectors
        return sparse_embedding

    norm = math.sqrt(sum(val * val for val in sparse_embedding.values))
    if norm > 1e-12:  # Avoid division by zero
        normalized_values = [val / norm for val in sparse_embedding.values]
    else:
        normalized_values = sparse_embedding.values  # Return as-is

    return SparseEmbedding(indices=sparse_embedding.indices, values=normalized_values)


def sparse_dot_product(sparse_emb1: SparseEmbedding, sparse_emb2: SparseEmbedding) -> float:
    """
    Computes the dot product between two sparse embeddings.
    Optimized for efficiency.

    Args:
        sparse_emb1: First sparse embedding
        sparse_emb2: Second sparse embedding

    Returns:
        Dot product value
    """
    if not sparse_emb1.indices or not sparse_emb2.indices:
        return 0.0

    # Use a dictionary for faster lookup (O(1) on average)
    emb2_dict = dict(zip(sparse_emb2.indices, sparse_emb2.values))
    dot_product = 0.0

    for i, val1 in zip(sparse_emb1.indices, sparse_emb1.values):
        if i in emb2_dict:
            dot_product += val1 * emb2_dict[i]

    return dot_product


def convert_to_sparse_embedding(dense_vector: Union[mx.array, np.ndarray], threshold: float = 1e-6) -> SparseEmbedding:
    """
    Convert a dense vector to sparse embedding format.
    
    Args:
        dense_vector: Dense vector as mx.array or numpy array
        threshold: Values below this threshold are considered zero
        
    Returns:
        SparseEmbedding representation
    """
    # If input is mx.array, convert to numpy
    if isinstance(dense_vector, mx.array):
        dense_np = np.array(dense_vector)
    else:
        dense_np = dense_vector
        
    # Find non-zero indices and values
    indices = np.nonzero(np.abs(dense_np) > threshold)[0].tolist()
    values = dense_np[indices].tolist()
    
    return SparseEmbedding(indices=indices, values=values)


class SparseModelArgs:
    """
    Arguments for sparse embedding models.
    """

    def __init__(self, **kwargs):
        """Initialize from kwargs."""
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def from_dict(cls, config: dict) -> "SparseModelArgs":
        """Create from a dictionary (usually loaded from config.json)."""
        return cls(**config)


class Model(nn.Module):
    """
    Simple wrapper for sparse embedding models.
    """

    def __init__(self, args: SparseModelArgs):
        """Initialize the model."""
        super().__init__()
        self.args = args
        # Initialize model components based on args
        # ...

    def __call__(self, input_ids, attention_mask=None):
        """Forward pass."""
        # Implement sparse model forward logic
        # This is a placeholder, actual implementation depends on model architecture
        return input_ids  # Placeholder

    def load_weights(self, weights):
        """Load weights."""
        # Implement weight loading
        # This is a placeholder
