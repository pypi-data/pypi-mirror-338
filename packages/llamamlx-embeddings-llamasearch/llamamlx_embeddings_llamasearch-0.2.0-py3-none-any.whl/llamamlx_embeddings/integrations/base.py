"""
Base class for vector database integrations.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..core.embeddings import BaseEmbedding


class VectorDBClient(ABC):
    """
    Abstract base class for vector database clients.
    """

    def __init__(self, embedding_model: BaseEmbedding, collection_name: str, **kwargs):
        """
        Initialize the vector database client.

        Args:
            embedding_model: Model for generating embeddings
            collection_name: Name of the collection/index to use
            **kwargs: Additional client-specific parameters
        """
        self.embedding_model = embedding_model
        self.collection_name = collection_name

    @abstractmethod
    def add(
        self,
        documents: List[str],
        metadata: Optional[List[Dict[str, Any]]] = None,
        ids: Optional[List[str]] = None,
        **kwargs,
    ) -> List[str]:
        """
        Add documents to the vector database.

        Args:
            documents: List of document texts
            metadata: Optional metadata for each document
            ids: Optional IDs for each document
            **kwargs: Additional parameters

        Returns:
            List of document IDs
        """

    @abstractmethod
    def query(
        self, query_text: str, limit: int = 10, filter: Optional[Dict[str, Any]] = None, **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Query the vector database.

        Args:
            query_text: The query text
            limit: Maximum number of results
            filter: Optional filter
            **kwargs: Additional parameters

        Returns:
            List of results with document texts, IDs, and scores
        """

    @abstractmethod
    def delete(
        self, ids: Optional[List[str]] = None, filter: Optional[Dict[str, Any]] = None, **kwargs
    ) -> int:
        """
        Delete documents from the vector database.

        Args:
            ids: List of document IDs to delete
            filter: Optional filter for documents to delete
            **kwargs: Additional parameters

        Returns:
            Number of documents deleted
        """
