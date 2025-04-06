#!/usr/bin/env python
"""
Basic example demonstrating how to use llamamlx-embeddings for text embeddings.
"""

import os
import sys
import time
import numpy as np

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings import (
    TextEmbedding,
    list_supported_models,
    configure_logging,
)
from llamamlx_embeddings.core.mock_embeddings import MockEmbedding


def main():
    """Run a basic embedding example."""
    # Set up logging
    configure_logging(level="INFO")

    # List available models
    print("Available models:")
    models = list_supported_models()
    for model_type, model_list in models.items():
        print(f"  {model_type.upper()}:")
        for model in model_list:
            print(f"    - {model}")
    print()

    # For quick testing, use the mock embedding 
    # In real usage, specify a real model name like "BAAI/bge-small-en-v1.5"
    print("Using mock embedding model for demonstration...")
    
    # Create an embedding model - directly use MockEmbedding for this example
    print("Creating embedding model...")
    mock_model = MockEmbedding(embedding_size=384)
    
    # Example texts
    texts = [
        "This is a sample text for embedding.",
        "Another example with different words.",
        "MLX provides fast computation on Apple Silicon.",
    ]
    
    # Generate embeddings
    print("\nGenerating embeddings for sample texts...")
    start_time = time.time()
    embeddings = mock_model.encode(texts)
    end_time = time.time()
    
    # Print embedding information
    print(f"Generated {len(embeddings)} embeddings in {end_time - start_time:.4f} seconds")
    print(f"Embedding dimension: {embeddings[0].shape}")
    print(f"First embedding preview: {embeddings[0][:5]}...\n")
    
    # Compute similarities
    print("Computing similarities between texts:")
    for i in range(len(texts)):
        for j in range(i+1, len(texts)):
            # Compute cosine similarity manually
            dot_product = np.dot(embeddings[i], embeddings[j])
            print(f"Similarity between text {i+1} and {j+1}: {dot_product:.4f}")
    
    # Query-document relevance example
    print("\nQuery-document relevance example:")
    query = "What is MLX?"
    query_embedding = mock_model.encode_query(query)
    
    print(f"Query: '{query}'")
    print("Document relevance scores:")
    for i, text in enumerate(texts):
        score = np.dot(query_embedding, embeddings[i])
        print(f"  Document {i+1}: {score:.4f} - '{text}'")


if __name__ == "__main__":
    main() 