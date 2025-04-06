#!/usr/bin/env python
"""
Example of performing semantic search with llamamlx-embeddings.
"""

import logging
import math
import numpy as np
from typing import Dict, List, Tuple, Any
import sys
import os

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings.core.mock_embeddings import MockEmbedding

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def compute_similarity(query_emb: np.ndarray, doc_embs: List[np.ndarray]) -> List[float]:
    """
    Compute cosine similarity between query and documents.
    
    Args:
        query_emb: Query embedding
        doc_embs: List of document embeddings
        
    Returns:
        List of similarity scores
    """
    # Compute dot product (vectors are already normalized)
    similarities = [np.dot(query_emb, doc_emb) for doc_emb in doc_embs]
    return similarities


def search(
    query: str,
    documents: List[Dict[str, Any]],
    model: MockEmbedding,
    top_k: int = 5,
) -> List[Dict[str, Any]]:
    """
    Perform semantic search on documents.
    
    Args:
        query: Search query
        documents: List of documents (each with "text" field)
        model: Embedding model
        top_k: Number of top results to return
        
    Returns:
        List of top documents with similarity scores
    """
    # Check if we have documents
    if not documents:
        logger.warning("No documents provided for search")
        return []
        
    # Get query embedding
    logger.info(f"Generating embedding for query: {query}")
    query_embedding = model.encode_query(query)
    
    # Get document texts
    doc_texts = [doc["text"] for doc in documents]
    
    # Get document embeddings
    logger.info(f"Generating embeddings for {len(doc_texts)} documents")
    doc_embeddings = model.encode_documents(doc_texts)
    
    # Compute similarities
    similarities = compute_similarity(query_embedding, doc_embeddings)
    
    # Create results with scores
    results = [
        {**documents[i], "score": float(similarities[i])}
        for i in range(len(documents))
    ]
    
    # Sort by score (descending)
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    
    # Return top_k results
    return results[:top_k]


def main():
    # Sample documents
    documents = [
        {"id": 1, "text": "The MLX framework is designed for Apple Silicon processors.", "source": "docs"},
        {"id": 2, "text": "Embeddings are vector representations of text or other data.", "source": "docs"},
        {"id": 3, "text": "Neural networks consist of layers of artificial neurons.", "source": "wiki"},
        {"id": 4, "text": "Apple Silicon processors use the ARM architecture.", "source": "wiki"},
        {"id": 5, "text": "Vector databases are specialized for storing and querying embeddings.", "source": "blog"},
        {"id": 6, "text": "Semantic search finds results based on meaning, not just keywords.", "source": "blog"},
        {"id": 7, "text": "MLX is optimized for running efficiently on Apple's M-series chips.", "source": "docs"},
        {"id": 8, "text": "BERT and other transformer models revolutionized NLP.", "source": "paper"},
        {"id": 9, "text": "Text embeddings capture semantic information in dense vectors.", "source": "paper"},
        {"id": 10, "text": "The M1 and M2 chips outperform many laptop processors in efficiency.", "source": "news"},
    ]
    
    print("\n" + "="*80)
    print("Semantic Search Example using Mock Embeddings")
    print("="*80)
    
    # Initialize mock embedding model
    model = MockEmbedding(embedding_size=384, model_id="mock-model")
    
    # Define a search query
    query = "How do embeddings work for semantic search?"
    
    print(f"\nQuery: {query}\n")
    
    # Perform search
    results = search(query, documents, model, top_k=3)
    
    # Display results
    print("\nTop 3 Results:")
    print("-" * 40)
    
    for i, result in enumerate(results, 1):
        print(f"{i}. Score: {result['score']:.4f}")
        print(f"   ID: {result['id']}")
        print(f"   Text: {result['text']}")
        print(f"   Source: {result['source']}")
        print()
        
    # Try another query
    query = "What is the MLX framework for Apple processors?"
    
    print(f"\nQuery: {query}\n")
    
    # Perform search
    results = search(query, documents, model, top_k=3)
    
    # Display results
    print("\nTop 3 Results:")
    print("-" * 40)
    
    for i, result in enumerate(results, 1):
        print(f"{i}. Score: {result['score']:.4f}")
        print(f"   ID: {result['id']}")
        print(f"   Text: {result['text']}")
        print(f"   Source: {result['source']}")
        print()
        

if __name__ == "__main__":
    main() 