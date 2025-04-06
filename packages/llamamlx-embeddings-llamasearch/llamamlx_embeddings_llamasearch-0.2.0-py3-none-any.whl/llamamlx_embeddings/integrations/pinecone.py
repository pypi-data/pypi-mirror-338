"""
Pinecone vector database integration.
"""

import logging
import uuid
from typing import Any, Dict, List, Optional

import numpy as np

# Import core modules with proper relative imports
from ..core.embeddings import BaseEmbedding, TextEmbedding
from ..core.sparse import SparseEmbedding 
from ..core.models import get_model_info
from ..utils.error_handling import safe_import, require_dependency
from .base import VectorDBClient

# Configure logging
logger = logging.getLogger(__name__)

# Safely import pinecone
pinecone = safe_import("pinecone", extra_name="pinecone")
PINECONE_AVAILABLE = pinecone is not None


class PineconeClient(VectorDBClient):
    """
    Client for Pinecone vector database integration.
    """

    def __init__(
        self,
        embedding_model: BaseEmbedding,
        collection_name: str,
        api_key: str,
        environment: str,
        namespace: str = "",
        **kwargs,
    ):
        """
        Initialize the Pinecone client.

        Args:
            embedding_model: Model for generating embeddings
            collection_name: Name of the index to use
            api_key: Pinecone API key
            environment: Pinecone environment
            namespace: Optional namespace
            **kwargs: Additional parameters for Pinecone client
        """
        super().__init__(embedding_model, collection_name)

        if not PINECONE_AVAILABLE:
            raise ImportError(
                "Pinecone client not installed. Install with 'pip install llamamlx-embeddings[pinecone]'"
            )

        self.namespace = namespace
        self.model_dims = self.embedding_model.model_info.get("dim", 384)

        # Initialize Pinecone
        pinecone.init(api_key=api_key, environment=environment)

        # Get or create index
        try:
            indexes = pinecone.list_indexes()

            if collection_name not in indexes:
                logger.info(f"Creating new index: {collection_name}")
                pinecone.create_index(
                    name=collection_name, dimension=self.model_dims, metric="cosine", **kwargs
                )
            else:
                logger.info(f"Using existing index: {collection_name}")

            # Connect to the index
            self.index = pinecone.Index(collection_name)

        except Exception as e:
            logger.error(f"Error initializing Pinecone index: {str(e)}")
            raise

    def add(
        self,
        documents: List[str],
        metadata: Optional[List[Dict[str, Any]]] = None,
        ids: Optional[List[str]] = None,
        batch_size: int = 64,
        **kwargs,
    ) -> List[str]:
        """
        Add documents to Pinecone.

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
            # Convert to numpy if needed
            batch_embs_np = [np.array(emb) for emb in batch_embs]
            embeddings.extend(batch_embs_np)

        # Add vectors to Pinecone
        logger.info(f"Adding {len(documents)} documents to Pinecone")

        vectors = []
        for i, (doc_id, doc_text, doc_meta, doc_emb) in enumerate(
            zip(ids, documents, metadata, embeddings)
        ):
            # Add text to metadata
            doc_meta["text"] = doc_text

            vector = (doc_id, doc_emb.tolist(), doc_meta)
            vectors.append(vector)

            # Upload in batches
            if len(vectors) >= batch_size or i == len(documents) - 1:
                self.index.upsert(vectors=vectors, namespace=self.namespace)
                logger.info(f"Uploaded batch of {len(vectors)} documents")
                vectors = []

        return ids

    def query(
        self, query_text: str, limit: int = 10, filter: Optional[Dict[str, Any]] = None, **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Query Pinecone.

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

        # Query Pinecone
        logger.info(f"Querying Pinecone with limit={limit}")
        results = self.index.query(
            vector=query_embedding_np.tolist(),
            top_k=limit,
            include_metadata=True,
            namespace=self.namespace,
            filter=filter,
            **kwargs,
        )

        # Format results
        formatted_results = []
        for match in results.matches:
            text = match.metadata.get("text", "")
            formatted_results.append(
                {
                    "id": match.id,
                    "text": text,
                    "score": match.score,
                    "metadata": {k: v for k, v in match.metadata.items() if k != "text"},
                }
            )

        return formatted_results

    def delete(
        self, ids: Optional[List[str]] = None, filter: Optional[Dict[str, Any]] = None, **kwargs
    ) -> int:
        """
        Delete documents from Pinecone.

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
            self.index.delete(
                ids=ids,
                namespace=self.namespace,
            )
            return len(ids)
        elif filter is not None:
            # Delete by filter
            # Note: Pinecone doesn't directly support deleting by filter
            # We have to query and then delete by IDs
            logger.info(f"Deleting documents by filter: {filter}")

            # Query to get IDs that match the filter
            results = self.index.query(
                vector=[0.0] * self.model_dims,  # Dummy vector
                top_k=10000,  # Get as many as possible
                include_metadata=False,
                filter=filter,
                namespace=self.namespace,
            )

            # Extract IDs
            ids_to_delete = [match.id for match in results.matches]

            if ids_to_delete:
                # Delete the IDs
                self.index.delete(
                    ids=ids_to_delete,
                    namespace=self.namespace,
                )

            return len(ids_to_delete)
        else:
            raise ValueError("Either ids or filter must be provided")
