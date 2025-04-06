#!/usr/bin/env python
"""
Basic usage examples for llamamlx-embeddings.
"""

import logging
import numpy as np
from typing import List
import time
import sys
import os

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# For demonstration purposes, use MockEmbedding instead of actual models
from llamamlx_embeddings.core.mock_embeddings import MockEmbedding

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def direct_embedding_example():
    """Example of directly using the embedding classes."""
    logger.info("Testing direct embedding:")
    
    # Create a mock embedding model
    print("Creating mock embedding model for demonstration...")
    model = MockEmbedding(embedding_size=384, model_id="mock-model")
    
    # Example texts
    query = "How to make a delicious pizza?"
    documents = [
        "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
        "To make pizza, you need flour, water, yeast, salt, olive oil, tomato sauce, and cheese.",
        "The history of pizza begins in antiquity, when various ancient cultures produced basic flatbreads with toppings.",
        "A recipe for making something completely different like a chocolate cake."
    ]
    
    # Embed query and documents
    query_embedding = model.encode_query(query)
    document_embeddings = model.encode_documents(documents)
    
    # Calculate similarities
    similarities = []
    for i, doc_emb in enumerate(document_embeddings):
        similarity = cosine_similarity(query_embedding, doc_emb)
        similarities.append(similarity)
        logger.info(f"Document {i+1} similarity: {similarity:.4f}")
    
    # Get most similar document
    most_similar_idx = np.argmax(similarities)
    logger.info(f"Most similar document: {most_similar_idx+1}")
    logger.info(f"Text: {documents[most_similar_idx]}")


def api_client_example():
    """
    Example of using the API client.
    
    Note: This is just a demonstration and would require the API server to be running.
    For this example script, we're using a mock implementation.
    """
    logger.info("\nTesting API client (mock implementation):")
    
    # Create a mock embedding function
    model = MockEmbedding(embedding_size=384, model_id="mock-model")
    
    # Example texts
    query = "How to make a delicious pizza?"
    documents = [
        "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
        "To make pizza, you need flour, water, yeast, salt, olive oil, tomato sauce, and cheese.",
        "The history of pizza begins in antiquity, when various ancient cultures produced basic flatbreads with toppings.",
        "A recipe for making something completely different like a chocolate cake."
    ]
    
    # Get query embedding
    query_embedding = model.encode_query(query)
    
    # Get document embeddings
    document_embeddings = model.encode_documents(documents)
    
    # Calculate similarities
    similarities = []
    for i, doc_emb in enumerate(document_embeddings):
        similarity = cosine_similarity(query_embedding, doc_emb)
        similarities.append(similarity)
        logger.info(f"Document {i+1} similarity: {similarity:.4f}")
    

def benchmark_example():
    """Simple benchmark of embedding generation."""
    logger.info("\nRunning simple benchmark:")
    
    model = MockEmbedding(embedding_size=384, model_id="mock-model")
    
    # Generate some test data
    num_samples = 100
    text_length = 100
    
    texts = [
        "This is a test document " * (text_length // 5)
        for _ in range(num_samples)
    ]
    
    # Benchmark
    start_time = time.time()
    for batch_start in range(0, len(texts), 32):
        batch_end = min(batch_start + 32, len(texts))
        batch = texts[batch_start:batch_end]
        
        _ = model.encode_documents(batch)
    
    end_time = time.time()
    
    # Calculate metrics
    total_time = end_time - start_time
    texts_per_second = num_samples / total_time
    chars_per_second = (num_samples * text_length) / total_time
    
    logger.info(f"Processed {num_samples} texts in {total_time:.2f} seconds")
    logger.info(f"Speed: {texts_per_second:.2f} texts/second")
    logger.info(f"Throughput: {chars_per_second:.2f} characters/second")


if __name__ == "__main__":
    print("\n" + "="*80)
    print("Basic Usage Examples using Mock Embeddings")
    print("="*80)
    
    # Run direct embedding example
    direct_embedding_example()
    
    # Run mock API client example
    api_client_example()
    
    # Run benchmark example
    benchmark_example() 