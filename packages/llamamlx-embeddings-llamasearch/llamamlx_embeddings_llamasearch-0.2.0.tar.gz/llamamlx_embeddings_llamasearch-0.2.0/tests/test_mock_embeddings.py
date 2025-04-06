"""
Tests for mock embeddings functionality.
"""

import os
import sys
import unittest
from typing import List

import numpy as np

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings.core.mock_embeddings import MockEmbedding


class TestMockEmbeddings(unittest.TestCase):
    """Test cases for mock embeddings."""

    def setUp(self):
        """Set up test fixtures."""
        self.model = MockEmbedding(embedding_size=384, model_id="test-mock-model")
        self.texts = [
            "This is a test text for embeddings.",
            "Another example text to encode.",
            "A third text for testing batch processing.",
        ]

    def test_init(self):
        """Test initialization of mock embedding model."""
        model = MockEmbedding(embedding_size=512, model_id="custom-mock")
        self.assertEqual(model.embedding_size, 512)
        self.assertEqual(model.model_id, "custom-mock")

        # Test with default values
        default_model = MockEmbedding()
        self.assertEqual(default_model.embedding_size, 768)
        self.assertEqual(default_model.model_id, "mock-embedding")

    def test_single_encoding(self):
        """Test encoding a single text."""
        text = "This is a test text."
        embedding = self.model.encode(text)

        # Verify shape
        self.assertEqual(embedding.shape, (384,))

        # Verify type
        self.assertEqual(embedding.dtype, np.float32)

        # Verify norm is approximately 1
        norm = np.linalg.norm(embedding)
        self.assertAlmostEqual(norm, 1.0, places=6)

    def test_batch_encoding(self):
        """Test encoding a batch of texts."""
        embeddings = self.model.encode(self.texts)

        # Verify shape
        self.assertEqual(len(embeddings), len(self.texts))
        self.assertEqual(embeddings[0].shape, (384,))

        # Verify each embedding is normalized
        for emb in embeddings:
            norm = np.linalg.norm(emb)
            self.assertAlmostEqual(norm, 1.0, places=6)

    def test_deterministic(self):
        """Test that embeddings are deterministic for the same text."""
        text = "This is a test text."
        embedding1 = self.model.encode(text)
        embedding2 = self.model.encode(text)

        # The same text should produce the same embedding
        np.testing.assert_array_equal(embedding1, embedding2)

    def test_different_embeddings(self):
        """Test that different texts produce different embeddings."""
        embedding1 = self.model.encode(self.texts[0])
        embedding2 = self.model.encode(self.texts[1])

        # Different texts should produce different embeddings
        self.assertFalse(np.array_equal(embedding1, embedding2))

    def test_query_embedding(self):
        """Test generating query embeddings."""
        text = "This is a query text."
        embedding = self.model.encode_query(text)

        # Verify shape
        self.assertEqual(embedding.shape, (384,))

        # Verify it's normalized
        norm = np.linalg.norm(embedding)
        self.assertAlmostEqual(norm, 1.0, places=6)

    def test_document_embedding(self):
        """Test generating document embeddings."""
        text = "This is a document text."
        embedding = self.model.encode_documents([text])[0]

        # Verify shape
        self.assertEqual(embedding.shape, (384,))

        # Verify it's normalized
        norm = np.linalg.norm(embedding)
        self.assertAlmostEqual(norm, 1.0, places=6)

    def test_query_vs_document(self):
        """Test that query and document embeddings for the same text are different."""
        text = "This is a test text."
        query_embedding = self.model.encode_query(text)
        doc_embedding = self.model.encode_documents([text])[0]

        # Should be different due to different random seeds
        self.assertFalse(np.array_equal(query_embedding, doc_embedding))

    def test_rerank(self):
        """Test document reranking functionality."""
        query = "Test query"
        docs = ["First document", "Second document", "Relevant test document"]

        scores = self.model.rerank(query, docs)

        # Verify we get a score for each document
        self.assertEqual(len(scores), len(docs))

        # Scores should be between 0 and 1
        for score in scores:
            self.assertGreaterEqual(score, 0.0)
            self.assertLessEqual(score, 1.0)

    def test_custom_seed(self):
        """Test setting a custom random seed."""
        model1 = MockEmbedding(embedding_size=128, random_seed=42)
        model2 = MockEmbedding(embedding_size=128, random_seed=42)
        model3 = MockEmbedding(embedding_size=128, random_seed=100)

        text = "Test with custom seed"

        # Models with the same seed should produce identical embeddings
        emb1 = model1.encode(text)
        emb2 = model2.encode(text)
        np.testing.assert_array_equal(emb1, emb2)

        # Models with different seeds should produce different embeddings
        emb3 = model3.encode(text)
        self.assertFalse(np.array_equal(emb1, emb3))


if __name__ == "__main__":
    unittest.main()
