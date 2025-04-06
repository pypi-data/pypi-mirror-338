#!/usr/bin/env python
"""
Example of semantic search using mock embeddings for testing.
"""

import logging
import numpy as np
from typing import List, Dict, Any, Tuple
import sys
import os

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings.core.mock_embeddings import MockEmbedding

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class SemanticSearch:
    """
    Simple semantic search implementation.
    """
    
    def __init__(self, embedding_model=None):
        """
        Initialize the semantic search.
        
        Args:
            embedding_model: Model to use for embeddings (optional)
        """
        # Use mock embedding model by default
        self.embedding_model = embedding_model or MockEmbedding(embedding_size=384)
        self.documents = []
        self.embeddings = []
        
    def add_documents(self, documents: List[str], metadata: List[Dict[str, Any]] = None):
        """
        Add documents to the search index.
        
        Args:
            documents: List of document texts
            metadata: Optional metadata for each document
        """
        if metadata is None:
            metadata = [{} for _ in documents]
            
        # Generate embeddings
        logger.info(f"Generating embeddings for {len(documents)} documents")
        document_embeddings = self.embedding_model.encode_documents(documents)
        
        # Store documents and embeddings
        for doc, emb, meta in zip(documents, document_embeddings, metadata):
            self.documents.append({"text": doc, "metadata": meta})
            self.embeddings.append(np.array(emb))
            
        logger.info(f"Added {len(documents)} documents to search index")
        
    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Search for documents similar to the query.
        
        Args:
            query: Query text
            top_k: Number of results to return
            
        Returns:
            List of results with text, metadata, and score
        """
        # Generate query embedding
        logger.info(f"Generating embedding for query: {query}")
        query_embedding = np.array(self.embedding_model.encode_query(query))
        
        # Calculate similarities
        similarities = []
        for i, doc_emb in enumerate(self.embeddings):
            similarity = cosine_similarity(query_embedding, doc_emb)
            similarities.append((i, similarity))
            
        # Sort by similarity (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Get top results
        results = []
        for i, score in similarities[:top_k]:
            results.append({
                "text": self.documents[i]["text"],
                "metadata": self.documents[i]["metadata"],
                "score": float(score)
            })
            
        return results


def main():
    """Run the semantic search example."""
    # Create a semantic search instance
    search = SemanticSearch()
    
    # Example documents
    documents = [
        "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
        "To make pizza, you need flour, water, yeast, salt, olive oil, tomato sauce, and cheese.",
        "The history of pizza begins in antiquity, when various ancient cultures produced basic flatbreads with toppings.",
        "A recipe for making something completely different like a chocolate cake.",
        "The iPhone is a smartphone made by Apple that combines a computer, iPod, digital camera, and cellular phone into one device.",
        "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability.",
        "Machine learning is a field of inquiry devoted to understanding and building methods that 'learn', that is, methods that leverage data to improve performance on some set of tasks.",
        "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language.",
    ]
    
    # Add metadata
    metadata = [
        {"category": "food", "subcategory": "pizza", "id": 1},
        {"category": "food", "subcategory": "pizza", "id": 2},
        {"category": "food", "subcategory": "pizza", "id": 3},
        {"category": "food", "subcategory": "dessert", "id": 4},
        {"category": "technology", "subcategory": "mobile", "id": 5},
        {"category": "technology", "subcategory": "programming", "id": 6},
        {"category": "technology", "subcategory": "AI", "id": 7},
        {"category": "technology", "subcategory": "AI", "id": 8},
    ]
    
    # Add documents to search index
    search.add_documents(documents, metadata)
    
    # Perform searches
    queries = [
        "How do I make pizza?",
        "Tell me about artificial intelligence and NLP",
        "What programming languages are popular?",
        "I want a dessert recipe"
    ]
    
    for query in queries:
        logger.info(f"\nSearching for: {query}")
        results = search.search(query, top_k=2)
        
        # Display results
        for i, result in enumerate(results):
            logger.info(f"Result {i+1}:")
            logger.info(f"Text: {result['text']}")
            logger.info(f"Category: {result['metadata']['category']}/{result['metadata']['subcategory']}")
            logger.info(f"Score: {result['score']:.4f}")


if __name__ == "__main__":
    main() 