"""
Mock embedding model for testing without requiring real models.
"""

import hashlib
import logging
from typing import List, Optional, Union

import numpy as np

# Configure logging
logger = logging.getLogger(__name__)


class MockEmbedding:
    """
    A mock embedding model that generates deterministic random embeddings for testing.

    This class simulates an embedding model without requiring any actual models
    or special hardware. It generates normalized random vectors based on the hash
    of the input text, ensuring deterministic behavior for the same inputs.
    """

    def __init__(
        self,
        embedding_size: int = 768,
        model_id: str = "mock-embedding",
        random_seed: Optional[int] = None,
    ):
        """
        Initialize a mock embedding model.

        Args:
            embedding_size: Size of the embedding vectors to generate
            model_id: Identifier for the mock model
            random_seed: Random seed for reproducibility
        """
        self.embedding_size = embedding_size
        self.model_id = model_id
        self.random_seed = random_seed
        self.query_prefix = "query: "
        self.doc_prefix = "document: "

        # Initialize seeds for different embedding types
        self._base_seed = random_seed if random_seed is not None else 42
        self._query_seed = self._base_seed + 1
        self._doc_seed = self._base_seed + 2

        logger.info(f"Initialized mock embedding model with size {embedding_size}")

    def encode(self, texts: Union[str, List[str]]) -> Union[np.ndarray, List[np.ndarray]]:
        """
        Generate mock embeddings for the input texts.

        Args:
            texts: Single text string or list of texts to embed

        Returns:
            Single embedding vector or list of embedding vectors
        """
        if isinstance(texts, str):
            return self._generate_embedding(texts, seed=self._base_seed)
        else:
            return [self._generate_embedding(text, seed=self._base_seed) for text in texts]

    def encode_query(self, text: str) -> np.ndarray:
        """
        Generate a mock query embedding.

        Args:
            text: Query text to embed

        Returns:
            Query embedding vector
        """
        return self._generate_embedding(self.query_prefix + text, seed=self._query_seed)

    def encode_documents(self, texts: List[str]) -> List[np.ndarray]:
        """
        Generate mock document embeddings.

        Args:
            texts: List of document texts to embed

        Returns:
            List of document embedding vectors
        """
        return [
            self._generate_embedding(self.doc_prefix + text, seed=self._doc_seed) for text in texts
        ]

    def rerank(self, query: str, documents: List[str]) -> List[float]:
        """
        Generate mock relevance scores for reranking.

        Args:
            query: Query text
            documents: List of document texts to score

        Returns:
            List of relevance scores (0-1) for each document
        """
        query_embedding = self.encode_query(query)
        doc_embeddings = self.encode_documents(documents)

        # Calculate cosine similarities
        scores = []
        for doc_emb in doc_embeddings:
            # Add some randomness based on the document hash
            doc_hash = int(hashlib.md5(doc_emb.tobytes()).hexdigest(), 16) % 100

            # Base score on vector similarity with some random noise
            similarity = np.dot(query_embedding, doc_emb)
            noise = np.sin(doc_hash / 10.0) * 0.2  # Deterministic noise
            score = (similarity + 1.0) / 2.0 + noise  # Scale to 0-1 range

            # Ensure score is in [0, 1] range
            score = max(0.0, min(1.0, score))
            scores.append(float(score))

        return scores

    def _generate_embedding(self, text: str, seed: int) -> np.ndarray:
        """
        Generate a deterministic mock embedding for a text.

        Args:
            text: Text to generate embedding for
            seed: Random seed to use

        Returns:
            Normalized embedding vector
        """
        # Create a deterministic seed based on text and base seed
        text_hash = int(hashlib.md5(text.encode("utf-8")).hexdigest(), 16)
        combined_seed = (text_hash + seed) % (2**32)

        # Initialize RNG with deterministic seed
        rng = np.random.RandomState(combined_seed)

        # Generate a random vector
        embedding = rng.randn(self.embedding_size).astype(np.float32)

        # Normalize to unit length
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm

        return embedding
