#!/usr/bin/env python
"""
Example demonstrating sparse embeddings with llamamlx-embeddings.
"""

import os
import sys
import time
import random
import numpy as np

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings import (
    configure_logging,
)
from llamamlx_embeddings.core.mock_embeddings import MockEmbedding
from llamamlx_embeddings.core.sparse import SparseEmbedding, sparse_dot_product


def create_mock_sparse_embedding(text: str, vocab_size: int = 30522, sparsity: float = 0.99) -> SparseEmbedding:
    """Create a mock sparse embedding for demonstration purposes."""
    # Use a deterministic seed based on the text
    seed = sum(ord(c) for c in text)
    random.seed(seed)
    
    # Determine how many elements will be non-zero
    n_elements = max(int(vocab_size * (1 - sparsity)), 5)  # At least 5 non-zero elements
    
    # Select random indices (sorted for consistency)
    indices = sorted(random.sample(range(vocab_size), n_elements))
    
    # Generate random values for those indices
    values = [random.random() * 2 - 1 for _ in range(n_elements)]
    
    # Normalize values
    norm = sum(v*v for v in values) ** 0.5
    values = [v/norm for v in values]
    
    return SparseEmbedding(indices=indices, values=values)


def main():
    """Run a sparse embedding example."""
    # Set up logging
    configure_logging(level="INFO")
    
    print("This example demonstrates sparse embeddings")
    print("For this example, we're using a mock implementation of sparse embeddings")
    print("In real usage, you would specify a real model like 'prithivida/Splade_PP_en_v1'")
    
    # For demonstration, we'll create mock sparse embeddings directly
    vocab_size = 30522  # Use BERT vocab size for example
    
    # Example texts
    texts = [
        "Sparse embeddings capture word importance through weights.",
        "Each token is assigned a weight in the vocabulary space.",
        "MLX provides efficient sparse operations for embeddings.",
    ]
    
    print("\nGenerating mock sparse embeddings for sample texts...")
    start_time = time.time()
    sparse_embeddings = [create_mock_sparse_embedding(text, vocab_size) for text in texts]
    end_time = time.time()
    
    # Print sparse embedding information
    print(f"Generated {len(sparse_embeddings)} sparse embeddings in {end_time - start_time:.4f} seconds")
    
    for i, embedding in enumerate(sparse_embeddings):
        print(f"\nEmbedding {i+1}:")
        print(f"  Text: '{texts[i]}'")
        print(f"  Number of non-zero elements: {len(embedding.indices)}")
        print(f"  Sparsity: {1.0 - len(embedding.indices)/vocab_size:.6f}")
        
        # Print a few top indices and their values
        if embedding.indices:
            # Sort by value (highest first)
            sorted_indices = sorted(
                range(len(embedding.values)), 
                key=lambda i: abs(embedding.values[i]), 
                reverse=True
            )
            
            print("  Top tokens by weight:")
            for idx in sorted_indices[:5]:
                token_idx = embedding.indices[idx]
                token_val = embedding.values[idx]
                # In a real application, you could get the actual token from tokenizer.decode([token_idx])
                print(f"    Token ID {token_idx}: {token_val:.6f}")
    
    # Compute similarities between sparse vectors
    print("\nComputing similarities between sparse vectors:")
    for i in range(len(sparse_embeddings)):
        for j in range(i+1, len(sparse_embeddings)):
            # Using sparse dot product for efficiency
            similarity = sparse_dot_product(
                sparse_embeddings[i], sparse_embeddings[j]
            )
            print(f"Similarity between text {i+1} and {j+1}: {similarity:.6f}")
    
    # Query example
    print("\nQuery example:")
    query = "How do sparse embeddings work?"
    query_embedding = create_mock_sparse_embedding(query, vocab_size)
    
    print(f"Query: '{query}'")
    print(f"Query embedding non-zero elements: {len(query_embedding.indices)}")
    
    print("Document relevance scores:")
    for i, text in enumerate(texts):
        # Using sparse dot product for relevance scoring
        score = sparse_dot_product(query_embedding, sparse_embeddings[i])
        print(f"  Document {i+1}: {score:.6f} - '{text}'")


if __name__ == "__main__":
    main() 