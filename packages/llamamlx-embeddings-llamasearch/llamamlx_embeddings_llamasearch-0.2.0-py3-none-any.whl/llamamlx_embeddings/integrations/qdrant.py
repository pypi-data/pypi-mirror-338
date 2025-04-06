"""
Qdrant vector database integration.
"""

import logging
import uuid
from typing import Any, Dict, List, Optional

import numpy as np

# Import core modules with explicit relative imports
from ..core.embeddings import BaseEmbedding, TextEmbedding
from ..core.models import get_model_info
from ..core.sparse import SparseEmbedding
from ..utils.error_handling import safe_import, require_dependency
from .base import VectorDBClient

# Configure logging
logger = logging.getLogger(__name__)

# Safely import Qdrant client
qdrant_client = safe_import("qdrant_client", extra_name="qdrant")
if qdrant_client:
    from qdrant_client import QdrantClient as QdrantBase
    from qdrant_client.http import models
    QDRANT_AVAILABLE = True
else:
    QDRANT_AVAILABLE = False
    # Create dummy classes for type checking
    class QdrantBase:
        pass
    class models:
        class Filter:
            pass
        class Distance:
            COSINE = "cosine"
        class VectorParams:
            def __init__(self, **kwargs):
                pass
        class PointStruct:
            def __init__(self, **kwargs):
                pass
        class PointIdsList:
            def __init__(self, **kwargs):
                pass
        class FilterSelector:
            def __init__(self, **kwargs):
                pass


class QdrantClient(VectorDBClient):
    """
    Client for Qdrant vector database integration.
    """

    def __init__(
        self,
        embedding_model: BaseEmbedding,
        collection_name: str,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        qdrant_path: Optional[str] = None,
        force_recreate: bool = False,
        **kwargs,
    ):
        """
        Initialize the Qdrant client.

        Args:
            embedding_model: Model for generating embeddings
            collection_name: Name of the collection to use
            url: URL of the Qdrant server (for cloud deployment)
            api_key: API key for Qdrant cloud
            qdrant_path: Path to local Qdrant database (for local deployment)
            force_recreate: Whether to force collection recreation
            **kwargs: Additional parameters for Qdrant client
        """
        super().__init__(embedding_model, collection_name)

        if not QDRANT_AVAILABLE:
            raise ImportError(
                "Qdrant client not installed. Install with 'pip install llamamlx-embeddings[qdrant]'"
            )

        # Initialize Qdrant client
        self.client = QdrantBase(url=url, api_key=api_key, path=qdrant_path)
        self.model_dims = self.embedding_model.model_info.get("dim", 384)

        # Create collection if it doesn't exist
        try:
            collections = self.client.get_collections().collections
            collection_names = [c.name for c in collections]

            if collection_name in collection_names and force_recreate:
                logger.info(f"Recreating collection: {collection_name}")
                self.client.delete_collection(collection_name=collection_name)
                self._create_collection()
            elif collection_name not in collection_names:
                logger.info(f"Creating new collection: {collection_name}")
                self._create_collection()
            else:
                logger.info(f"Using existing collection: {collection_name}")

        except Exception as e:
            logger.error(f"Error initializing Qdrant collection: {str(e)}")
            raise

    def _create_collection(self):
        """Create a new Qdrant collection."""
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(
                size=self.model_dims,
                distance=models.Distance.COSINE,
            ),
        )
        logger.info(f"Created collection: {self.collection_name}")

    def add(
        self,
        documents: List[str],
        metadata: Optional[List[Dict[str, Any]]] = None,
        ids: Optional[List[str]] = None,
        batch_size: int = 64,
        **kwargs,
    ) -> List[str]:
        """
        Add documents to Qdrant.

        Args:
            documents: List of document texts
            metadata: Optional metadata for each document
            ids: Optional IDs for each document
            batch_size: Batch size for processing
            **kwargs: Additional parameters

        Returns:
            List of document IDs
        """
        # Generate default IDs if not provided
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in range(len(documents))]

        # Use empty metadata if not provided
        if metadata is None:
            metadata = [{} for _ in range(len(documents))]

        # Validate input lengths
        if len(documents) != len(metadata) or len(documents) != len(ids):
            raise ValueError("documents, metadata, and ids must have the same length")

        # Generate embeddings
        logger.info(f"Generating embeddings for {len(documents)} documents")
        embeddings = []
        for batch_docs in [
            documents[i : i + batch_size] for i in range(0, len(documents), batch_size)
        ]:
            batch_embs = self.embedding_model.embed_documents(batch_docs)
            # Convert mx.array to numpy for Qdrant
            batch_embs_np = [np.array(emb) for emb in batch_embs]
            embeddings.extend(batch_embs_np)

        # Add points to Qdrant
        logger.info(f"Adding {len(documents)} documents to Qdrant")
        points = []
        for i, (doc_id, doc_text, doc_meta, doc_emb) in enumerate(
            zip(ids, documents, metadata, embeddings)
        ):
            # Add text to metadata
            doc_meta["text"] = doc_text

            point = models.PointStruct(id=doc_id, vector=doc_emb.tolist(), payload=doc_meta)
            points.append(point)

            # Upload in batches
            if len(points) >= batch_size or i == len(documents) - 1:
                self.client.upsert(collection_name=self.collection_name, points=points)
                logger.info(f"Uploaded batch of {len(points)} documents")
                points = []

        return ids

    def query(
        self, query_text: str, limit: int = 10, filter: Optional[Dict[str, Any]] = None, **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Query Qdrant.

        Args:
            query_text: The query text
            limit: Maximum number of results
            filter: Optional filter
            **kwargs: Additional parameters

        Returns:
            List of results with document texts, IDs, and scores
        """
        # Generate query embedding
        logger.info(f"Generating embedding for query: {query_text}")
        query_embedding = self.embedding_model.embed_query(query_text)
        query_embedding_np = np.array(query_embedding).astype(np.float32)

        # Convert filter to Qdrant format if provided
        qdrant_filter = None
        if filter:
            qdrant_filter = models.Filter(**filter)

        # Query Qdrant
        logger.info(f"Querying Qdrant with limit={limit}")
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding_np.tolist(),
            limit=limit,
            filter=qdrant_filter,
            with_payload=True,
            **kwargs,
        )

        # Format results
        formatted_results = []
        for res in results:
            text = res.payload.get("text", "")
            formatted_results.append(
                {
                    "id": res.id,
                    "text": text,
                    "score": res.score,
                    "metadata": {k: v for k, v in res.payload.items() if k != "text"},
                }
            )

        return formatted_results

    def delete(
        self, ids: Optional[List[str]] = None, filter: Optional[Dict[str, Any]] = None, **kwargs
    ) -> int:
        """
        Delete documents from Qdrant.

        Args:
            ids: List of document IDs to delete
            filter: Optional filter for documents to delete
            **kwargs: Additional parameters

        Returns:
            Number of documents deleted
        """
        if ids is not None:
            # Delete by IDs
            logger.info(f"Deleting {len(ids)} documents by ID")
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=models.PointIdsList(
                    points=ids,
                ),
            )
            return len(ids)
        elif filter is not None:
            # Delete by filter
            logger.info(f"Deleting documents by filter: {filter}")
            qdrant_filter = models.Filter(**filter)
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=models.FilterSelector(
                    filter=qdrant_filter,
                ),
            )
            # Note: Qdrant doesn't return the count of deleted documents
            return 0  # Placeholder
        else:
            raise ValueError("Either ids or filter must be provided")
