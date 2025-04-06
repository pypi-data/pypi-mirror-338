#!/usr/bin/env python
"""
Example of computing document similarity using llamamlx-embeddings.
"""

import logging
import numpy as np
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
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


def compute_similarity_matrix(doc_embeddings: List[np.ndarray]) -> np.ndarray:
    """
    Compute cosine similarity matrix between all documents.
    
    Args:
        doc_embeddings: List of document embeddings
        
    Returns:
        Similarity matrix (n_docs × n_docs)
    """
    n_docs = len(doc_embeddings)
    similarity_matrix = np.zeros((n_docs, n_docs))
    
    # Compute pairwise similarities
    for i in range(n_docs):
        for j in range(n_docs):
            # Compute dot product (vectors are already normalized)
            similarity_matrix[i, j] = np.dot(doc_embeddings[i], doc_embeddings[j])
            
    return similarity_matrix


def find_most_similar_pairs(
    documents: List[Dict], 
    similarity_matrix: np.ndarray,
    top_k: int = 5
) -> List[Tuple[Dict, Dict, float]]:
    """
    Find most similar document pairs based on similarity matrix.
    
    Args:
        documents: List of documents
        similarity_matrix: Document similarity matrix
        top_k: Number of top pairs to return
        
    Returns:
        List of tuples (doc1, doc2, similarity_score)
    """
    n_docs = len(documents)
    pairs = []
    
    # Collect all pairs and their similarities
    for i in range(n_docs):
        for j in range(i+1, n_docs):  # Start from i+1 to avoid duplicates and self-comparisons
            similarity = similarity_matrix[i, j]
            pairs.append((documents[i], documents[j], similarity))
    
    # Sort by similarity (descending)
    pairs.sort(key=lambda x: x[2], reverse=True)
    
    # Return top_k pairs
    return pairs[:top_k]


def visualize_similarity_matrix(
    similarity_matrix: np.ndarray,
    document_labels: List[str],
    title: str = "Document Similarity Matrix"
):
    """
    Visualize document similarity matrix as a heatmap.
    
    Args:
        similarity_matrix: Document similarity matrix
        document_labels: Labels for documents
        title: Plot title
    """
    plt.figure(figsize=(10, 8))
    plt.imshow(similarity_matrix, cmap='viridis', vmin=0, vmax=1)
    plt.colorbar(label='Cosine Similarity')
    
    # Add labels
    plt.xticks(range(len(document_labels)), document_labels, rotation=45, ha='right')
    plt.yticks(range(len(document_labels)), document_labels)
    
    # Add title and labels
    plt.title(title)
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('document_similarity_matrix.png')
    print("Similarity matrix visualization saved as 'document_similarity_matrix.png'")


def main():
    # Sample documents from different domains
    documents = [
        {"id": 1, "text": "The MLX framework is designed for Apple Silicon processors.", "category": "Tech"},
        {"id": 2, "text": "Apple Silicon processors use the ARM architecture.", "category": "Tech"},
        {"id": 3, "text": "MLX is optimized for running efficiently on Apple's M-series chips.", "category": "Tech"},
        {"id": 4, "text": "Neural networks consist of layers of artificial neurons.", "category": "AI"},
        {"id": 5, "text": "BERT and other transformer models revolutionized NLP.", "category": "AI"},
        {"id": 6, "text": "Embeddings are vector representations of text or other data.", "category": "AI"},
        {"id": 7, "text": "Text embeddings capture semantic information in dense vectors.", "category": "AI"},
        {"id": 8, "text": "Semantic search finds results based on meaning, not just keywords.", "category": "Search"},
        {"id": 9, "text": "Vector databases are specialized for storing and querying embeddings.", "category": "Search"},
        {"id": 10, "text": "The M1 and M2 chips outperform many laptop processors in efficiency.", "category": "Tech"},
    ]
    
    print("\n" + "="*80)
    print("Document Similarity Example using Mock Embeddings")
    print("="*80)
    
    # Initialize mock embedding model
    model = MockEmbedding(embedding_size=384, model_id="mock-model")
    
    # Extract document texts
    doc_texts = [doc["text"] for doc in documents]
    
    # Generate document embeddings
    logger.info(f"Generating embeddings for {len(doc_texts)} documents")
    doc_embeddings = model.encode_documents(doc_texts)
    
    # Compute similarity matrix
    logger.info("Computing document similarity matrix")
    similarity_matrix = compute_similarity_matrix(doc_embeddings)
    
    # Find most similar document pairs
    top_pairs = find_most_similar_pairs(documents, similarity_matrix, top_k=5)
    
    # Display results
    print("\nTop 5 Most Similar Document Pairs:")
    print("-" * 80)
    
    for i, (doc1, doc2, similarity) in enumerate(top_pairs, 1):
        print(f"{i}. Similarity Score: {similarity:.4f}")
        print(f"   Document 1 (ID: {doc1['id']}, Category: {doc1['category']}): {doc1['text']}")
        print(f"   Document 2 (ID: {doc2['id']}, Category: {doc2['category']}): {doc2['text']}")
        print()
    
    # Create document labels for visualization
    doc_labels = [f"Doc {doc['id']} ({doc['category']})" for doc in documents]
    
    # Visualize similarity matrix
    try:
        visualize_similarity_matrix(similarity_matrix, doc_labels)
    except ImportError:
        print("Note: Matplotlib is required for visualization. Install it with 'pip install matplotlib'")


if __name__ == "__main__":
    main() 