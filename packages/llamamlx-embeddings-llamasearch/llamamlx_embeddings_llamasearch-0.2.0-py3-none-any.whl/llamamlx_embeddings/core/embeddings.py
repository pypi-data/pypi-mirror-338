"""
Core embedding classes for text (and eventually image) embeddings.
"""

import logging
import os
from abc import ABC, abstractmethod
from typing import (
    Any,
    Iterable,
    List,
    Optional,
    Protocol,
    Union,
    runtime_checkable,
)

import mlx.core as mx
import numpy as np
from transformers import PreTrainedTokenizer

# Import models with relative imports to avoid Pylance errors
from .models import (
    DEFAULT_MODEL,
    get_model_info,
    get_model_path,
    load_mlx_model,
)
# Import sparse utilities
from .sparse import (
    SparseEmbedding,
    sparse_normalize,
    convert_to_sparse_embedding,
)

# Configure logging
logger = logging.getLogger(__name__)


def mean_pooling(input_array: mx.array) -> mx.array:
    """
    Compute mean pooling over the token dimension (dim=1).

    Args:
        input_array: Input tensor of shape [batch_size, seq_len, hidden_size]

    Returns:
        Mean pooled tensor of shape [batch_size, hidden_size]
    """
    return mx.mean(input_array, axis=1)


def normalize(input_array: mx.array) -> mx.array:
    """
    Normalize vectors to unit length.

    Args:
        input_array: Input tensor

    Returns:
        Normalized tensor
    """
    norm = mx.linalg.norm(input_array, axis=-1, keepdims=True)
    return input_array / (norm + 1e-12)


def iter_batch(iterable: List, batch_size: int) -> Iterable:
    """
    Yields batches of a specified size from an iterable.
    Handles non-divisible lengths.

    Args:
        iterable: The input list or iterable
        batch_size: Size of each batch

    Yields:
        Batches of the specified size
    """
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:  # Yield any remaining items
        yield batch


class BaseEmbedding(ABC):
    """
    Abstract base class for embedding models.
    """

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL,
        normalize: bool = True,
        cache_dir: Optional[str] = None,
        **kwargs,
    ):
        """
        Initialize the embedding model.

        Args:
            model_name: Name or path of the model
            normalize: Whether to normalize embeddings to unit length
            cache_dir: Directory to cache models
            **kwargs: Additional arguments for model loading
        """
        self.model_name = model_name
        self.normalize = normalize
        self.cache_dir = cache_dir
        self.kwargs = kwargs

        # Get model info (dimensions, type, etc.)
        if model_name != "mock" and not hasattr(self, "model_info"):  # Skip for mock models
            self.model_info = get_model_info(model_name)
            if self.model_info is None:
                raise ValueError(
                    f"Model '{model_name}' is not supported. See `list_supported_models()`."
                )

        self._model = None
        self._tokenizer = None

        # Load model immediately
        self.load_model()  # Load immediately

    @abstractmethod
    def load_model(self):
        """Loads the model and tokenizer."""
        ...

    @abstractmethod
    def embed(
        self,
        inputs: Union[str, List[str], Iterable[str]],
        batch_size: int = 32,
        **kwargs,
    ) -> Iterable[mx.array]:
        """
        Generates embeddings for the given inputs.

        Args:
            inputs: The input text(s) or a generator of texts
            batch_size: The batch size for processing
            **kwargs: Additional arguments for embedding generation

        Yields:
            Embeddings as mx.array objects
        """
        ...

    def _process_input(self, inputs: Union[str, List[str], Iterable[str]]):
        """
        Helper to handle different input types consistently.

        Args:
            inputs: Input text or list of texts

        Returns:
            Processed inputs as an iterable
        """
        if isinstance(inputs, str):
            inputs = [inputs]  # Single string -> list of one string
        return inputs  # Now it's always an iterable.


class TextEmbedding(BaseEmbedding):
    """
    Class for dense text embeddings using MLX.
    Supports various dense embedding models.
    """

    def load_model(self):
        """Load the model and tokenizer for dense embeddings."""
        quantize = self.kwargs.get("quantize", False)
        self._model, self._tokenizer = load_mlx_model(
            self.model_name, quantize=quantize, model_type="dense"
        )

    def embed(
        self,
        inputs: Union[str, List[str], Iterable[str]],
        batch_size: int = 32,
        **kwargs,
    ) -> Iterable[mx.array]:
        """
        Generate embeddings for the given text inputs.

        Args:
            inputs: Input text or list of texts
            batch_size: Batch size for processing
            **kwargs: Additional arguments for embedding generation

        Yields:
            Embeddings for each input or batch
        """
        inputs = self._process_input(inputs)

        for batch in iter_batch(inputs, batch_size):
            # Handle query/passage prefixes *inside* the batch loop
            prefixed_batch = []
            for text in batch:
                if text.startswith("query:") or text.startswith("passage:"):
                    prefixed_batch.append(text)  # Already prefixed
                elif self.model_name.startswith("BAAI/bge") or self.model_name.startswith(
                    "intfloat/e5"
                ):
                    #  This is where the logic from open-text-embeddings is crucial
                    if kwargs.get("is_passage", True):  # Default to passage if not specified
                        prefixed_batch.append("passage: " + text)
                    else:  # Otherwise, assume query
                        prefixed_batch.append("query: " + text)
                else:
                    prefixed_batch.append(text)  # No prefixing needed

            try:
                inputs_encoded = self._tokenizer(
                    prefixed_batch,
                    padding=True,
                    truncation=True,
                    return_tensors="np",
                    max_length=kwargs.get("max_length", 512),
                )

                input_ids = mx.array(inputs_encoded["input_ids"])
                attention_mask = mx.array(inputs_encoded["attention_mask"])

                # MLX model forward pass
                outputs = self._model(input_ids, attention_mask=attention_mask)

                # Mean pooling over token dimension
                embeddings = mean_pooling(outputs[0])

                # Normalize if requested
                if self.normalize:
                    embeddings = normalize(embeddings)

                yield embeddings

            except Exception as e:
                logger.error(f"Error generating embeddings: {str(e)}")
                raise

    def embed_query(self, query: str, **kwargs) -> mx.array:
        """
        Embed a single query text, handling prefixing correctly.

        Args:
            query: Query text to embed
            **kwargs: Additional arguments

        Returns:
            Query embedding
        """
        kwargs["is_passage"] = False
        return next(self.embed(query, **kwargs))[0]  # Return first embedding in batch

    def embed_documents(self, documents: List[str], **kwargs) -> List[mx.array]:
        """
        Embed a list of documents, handling prefixing correctly.

        Args:
            documents: List of document texts
            **kwargs: Additional arguments

        Returns:
            List of document embeddings
        """
        kwargs["is_passage"] = True
        return next(self.embed(documents, **kwargs))


class SparseTextEmbedding(BaseEmbedding):
    """
    Class for sparse text embeddings using MLX.
    Supports SPLADE and similar sparse models.
    """

    def load_model(self):
        """Load the model and tokenizer for sparse embeddings."""
        quantize = self.kwargs.get("quantize", False)
        self._model, self._tokenizer = load_mlx_model(
            self.model_name, quantize=quantize, model_type="sparse"
        )

    def embed(
        self,
        inputs: Union[str, List[str], Iterable[str]],
        batch_size: int = 2,  # SPLADE can be memory intensive, smaller batch
        **kwargs,
    ) -> Iterable[SparseEmbedding]:
        """
        Generate sparse embeddings for the given text inputs.

        Args:
            inputs: Input text or list of texts
            batch_size: Batch size for processing (generally smaller for sparse models)
            **kwargs: Additional arguments for embedding generation

        Yields:
            SparseEmbedding objects for each input or batch
        """
        inputs = self._process_input(inputs)

        for batch in iter_batch(inputs, batch_size):
            try:
                inputs_encoded = self._tokenizer(
                    batch,
                    padding=True,
                    truncation=True,
                    return_tensors="np",
                    max_length=kwargs.get("max_length", 512),
                )

                input_ids = mx.array(inputs_encoded["input_ids"])
                attention_mask = mx.array(inputs_encoded["attention_mask"])

                # MLX model forward pass - the output is the sparse activation
                outputs = self._model(input_ids, attention_mask=attention_mask)

                # Get raw sparse vectors (typically log(1 + ReLU(x)) activations)
                sparse_vecs = outputs[0]

                # For SPLADE models: get vocab size from tokenizer
                vocab_size = self._tokenizer.vocab_size

                # Process each vector into a SparseEmbedding
                for vec in sparse_vecs:
                    # Flatten to 1D if needed (this handles SPLADE's per-token activations)
                    if len(vec.shape) > 1:
                        # For SPLADE: max-pooling over tokens to get word importances
                        vec = mx.max(vec, axis=0)

                    # Convert to SparseEmbedding format
                    threshold = kwargs.get("threshold", 0.0)  # Threshold for sparsity (0 keeps all)
                    sparse_emb = SparseEmbedding.from_dense(vec, threshold=threshold)

                    # Normalize if requested
                    if self.normalize:
                        sparse_emb = sparse_normalize(sparse_emb)

                    yield sparse_emb

            except Exception as e:
                logger.error(f"Error generating sparse embeddings: {str(e)}")
                raise


class LateInteractionTextEmbedding(BaseEmbedding):
    """
    Class for late interaction (ColBERT-style) text embeddings using MLX.
    Produces per-token embeddings rather than a single vector.
    """

    def load_model(self):
        """Load the model and tokenizer for late interaction embeddings."""
        quantize = self.kwargs.get("quantize", False)
        self._model, self._tokenizer = load_mlx_model(
            self.model_name, quantize=quantize, model_type="late_interaction"
        )

    def embed(
        self,
        inputs: Union[str, List[str], Iterable[str]],
        batch_size: int = 32,
        **kwargs,
    ) -> Iterable[mx.array]:
        """
        Generate per-token embeddings for the given text inputs.

        Args:
            inputs: Input text or list of texts
            batch_size: Batch size for processing
            **kwargs: Additional arguments for embedding generation

        Yields:
            Per-token embeddings for each input (shape: [seq_len, dim])
        """
        inputs = self._process_input(inputs)

        for batch in iter_batch(inputs, batch_size):
            try:
                # Add [Q] prefix for queries, [D] for documents (ColBERT convention)
                prefixed_batch = []
                for text in batch:
                    if text.startswith("[Q]") or text.startswith("[D]"):
                        prefixed_batch.append(text)  # Already prefixed
                    else:
                        prefix = "[Q] " if kwargs.get("is_query", False) else "[D] "
                        prefixed_batch.append(prefix + text)

                inputs_encoded = self._tokenizer(
                    prefixed_batch,
                    padding="max_length",  # Fixed length for late interaction
                    truncation=True,
                    return_tensors="np",
                    max_length=kwargs.get("max_length", 512),
                )

                input_ids = mx.array(inputs_encoded["input_ids"])
                attention_mask = mx.array(inputs_encoded["attention_mask"])

                # MLX model forward pass
                token_embeddings = self._model(input_ids, attention_mask=attention_mask)[0]

                # Process each sequence of token embeddings
                for i, token_emb in enumerate(token_embeddings):
                    # Get the valid tokens using the attention mask
                    mask = attention_mask[i]
                    valid_length = mx.sum(mask).item()

                    # Only keep embeddings for valid tokens
                    valid_token_emb = token_emb[:valid_length]

                    # Normalize each token embedding if requested
                    if self.normalize:
                        valid_token_emb = normalize(valid_token_emb)

                    yield valid_token_emb

            except Exception as e:
                logger.error(f"Error generating late interaction embeddings: {str(e)}")
                raise


class TextCrossEncoder(BaseEmbedding):
    """
    Cross-encoder for scoring query-document pairs.
    Used for re-ranking in retrieval pipelines.
    """

    def load_model(self):
        """Load the cross-encoder model and tokenizer."""
        quantize = self.kwargs.get("quantize", False)
        self._model, self._tokenizer = load_mlx_model(
            self.model_name, quantize=quantize, model_type="cross_encoder"
        )

    def embed(
        self, inputs: Union[str, List[str], Iterable[str]], batch_size: int = 32, **kwargs
    ) -> Iterable[mx.array]:
        """Not really applicable for cross-encoders but implemented for consistency."""
        raise NotImplementedError(
            "Cross-encoders don't support independent text embedding. Use rerank() instead."
        )

    def rerank(self, query: str, documents: List[str], batch_size: int = 32) -> List[float]:
        """
        Rerank documents based on their relevance to the query.

        Args:
            query: Query text
            documents: List of document texts to rerank
            batch_size: Batch size for processing

        Returns:
            List of relevance scores for each document
        """
        # Prepare query-document pairs
        pairs = []
        for doc in documents:
            # Format for cross-encoder: "[CLS] query [SEP] document [SEP]"
            pairs.append(query + " [SEP] " + doc)

        scores = []

        for batch in iter_batch(pairs, batch_size):
            try:
                inputs_encoded = self._tokenizer(
                    batch,
                    padding=True,
                    truncation=True,
                    return_tensors="np",
                    max_length=512,
                )

                input_ids = mx.array(inputs_encoded["input_ids"])
                attention_mask = mx.array(inputs_encoded["attention_mask"])

                # MLX model forward pass
                outputs = self._model(input_ids, attention_mask=attention_mask)

                # For cross-encoders, typically the first logit is used as the score
                # This depends on the exact model architecture
                batch_scores = outputs[0]

                if len(batch_scores.shape) > 1 and batch_scores.shape[1] > 1:
                    # If model outputs multiple scores (usually 2), take the positive class score
                    batch_scores = batch_scores[:, 1]

                scores.extend(batch_scores.tolist())

            except Exception as e:
                logger.error(f"Error during reranking: {str(e)}")
                raise

        return scores


@runtime_checkable
class EmbeddingModel(Protocol):
    """Protocol defining the interface for embedding models."""

    model_id: str

    def encode(self, texts: Union[str, List[str]]) -> Union[np.ndarray, List[np.ndarray]]:
        """
        Encode text(s) into embeddings.

        Args:
            texts: Text or list of texts to encode

        Returns:
            Embedding vector(s)
        """
        ...

    def encode_query(self, text: str) -> np.ndarray:
        """
        Encode a query text into an embedding.

        Args:
            text: Query text to encode

        Returns:
            Query embedding vector
        """
        ...

    def encode_documents(self, texts: List[str]) -> List[np.ndarray]:
        """
        Encode document texts into embeddings.

        Args:
            texts: List of document texts to encode

        Returns:
            List of document embedding vectors
        """
        ...

    def rerank(self, query: str, documents: List[str]) -> List[float]:
        """
        Rerank documents based on relevance to query.

        Args:
            query: Query text
            documents: List of document texts to rerank

        Returns:
            List of relevance scores (0-1) for each document
        """
        ...


class MLXEmbeddingModel:
    """
    MLX-based embedding model implementation.

    This class wraps MLX models for generating embeddings efficiently
    on Apple Silicon hardware.
    """

    def __init__(
        self,
        model_id: str,
        model: Any,
        tokenizer: PreTrainedTokenizer,
        embedding_size: int,
        normalize: bool = True,
        pooling_strategy: str = "mean",
        max_length: Optional[int] = None,
    ):
        """
        Initialize an MLX embedding model.

        Args:
            model_id: Model identifier
            model: MLX model instance
            tokenizer: Tokenizer for the model
            embedding_size: Size of embeddings produced by the model
            normalize: Whether to normalize embeddings to unit length
            pooling_strategy: Strategy for pooling token embeddings ("mean", "cls", etc.)
            max_length: Maximum sequence length for tokenization
        """
        self.model_id = model_id
        self.model = model
        self.tokenizer = tokenizer
        self.embedding_size = embedding_size
        self.normalize = normalize
        self.pooling_strategy = pooling_strategy
        self.max_length = max_length or self.tokenizer.model_max_length

        # Special token handling for some models
        self.has_cls_token = "[CLS]" in self.tokenizer.special_tokens_map.get("cls_token", "")
        self.cls_token_id = self.tokenizer.cls_token_id

        logger.info(f"Initialized MLX embedding model: {model_id}")
        logger.info(f"Embedding size: {embedding_size}, Pooling: {pooling_strategy}")

    def encode(self, texts: Union[str, List[str]]) -> Union[np.ndarray, List[np.ndarray]]:
        """
        Encode text(s) into embeddings.

        Args:
            texts: Text or list of texts to encode

        Returns:
            Embedding vector(s)
        """
        # Handle single text
        if isinstance(texts, str):
            return self._encode_single(texts)

        # Handle batch of texts
        return self._encode_batch(texts)

    def encode_query(self, text: str) -> np.ndarray:
        """
        Encode a query text into an embedding.

        Args:
            text: Query text to encode

        Returns:
            Query embedding vector
        """
        # Some models have special handling for queries
        if hasattr(self.model, "encode_queries"):
            return self.model.encode_queries([text])[0]

        # Default to standard encoding
        return self._encode_single(text)

    def encode_documents(self, texts: List[str]) -> List[np.ndarray]:
        """
        Encode document texts into embeddings.

        Args:
            texts: List of document texts to encode

        Returns:
            List of document embedding vectors
        """
        # Some models have special handling for documents
        if hasattr(self.model, "encode_documents"):
            return self.model.encode_documents(texts)

        # Default to standard batch encoding
        return self._encode_batch(texts)

    def rerank(self, query: str, documents: List[str]) -> List[float]:
        """
        Rerank documents based on relevance to query.

        Args:
            query: Query text
            documents: List of document texts to rerank

        Returns:
            List of relevance scores (0-1) for each document
        """
        # Cross-encoder models may have direct reranking capability
        if hasattr(self.model, "compute_scores"):
            return self.model.compute_scores(query, documents)

        # Default to vector similarity
        query_embedding = self.encode_query(query)
        doc_embeddings = self.encode_documents(documents)

        # Compute cosine similarities
        scores = []
        for doc_emb in doc_embeddings:
            # Cosine similarity
            sim = np.dot(query_embedding, doc_emb)
            # Scale to 0-1 range
            score = (sim + 1.0) / 2.0
            scores.append(float(score))

        return scores

    def _encode_single(self, text: str) -> np.ndarray:
        """
        Encode a single text into an embedding.

        Args:
            text: Text to encode

        Returns:
            Embedding vector
        """
        # Tokenize the text
        encoded = self.tokenizer(
            text,
            return_tensors="np",
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
        )

        # Convert to MLX arrays
        inputs = {k: mx.array(v) for k, v in encoded.items()}

        # Forward pass through the model
        outputs = self.model(**inputs)

        # Extract embeddings based on pooling strategy
        if self.pooling_strategy == "cls" and self.has_cls_token:
            # Use CLS token embedding
            emb = outputs.last_hidden_state[:, 0]
        elif self.pooling_strategy == "mean":
            # Mean pooling over tokens (mask out padding)
            attention_mask = inputs["attention_mask"]
            emb = mx.sum(outputs.last_hidden_state * attention_mask.reshape(-1, 1), axis=1)
            emb = emb / mx.sum(attention_mask)
        else:
            # Default to first token if strategy is unknown
            emb = outputs.last_hidden_state[:, 0]

        # Convert to numpy and reshape
        embedding = emb.squeeze().astype(mx.float32)

        # Normalize if needed
        if self.normalize:
            embedding = embedding / mx.linalg.norm(embedding)

        # Convert to numpy
        return np.array(embedding)

    def _encode_batch(self, texts: List[str]) -> List[np.ndarray]:
        """
        Encode a batch of texts into embeddings.

        Args:
            texts: List of texts to encode

        Returns:
            List of embedding vectors
        """
        # Tokenize the texts
        encoded = self.tokenizer(
            texts,
            return_tensors="np",
            max_length=self.max_length,
            padding=True,
            truncation=True,
        )

        # Convert to MLX arrays
        inputs = {k: mx.array(v) for k, v in encoded.items()}

        # Forward pass through the model
        outputs = self.model(**inputs)

        # Extract embeddings based on pooling strategy
        if self.pooling_strategy == "cls" and self.has_cls_token:
            # Use CLS token embedding
            embeddings = outputs.last_hidden_state[:, 0]
        elif self.pooling_strategy == "mean":
            # Mean pooling over tokens (mask out padding)
            attention_mask = inputs["attention_mask"].reshape(len(texts), -1, 1)
            token_embeddings = outputs.last_hidden_state
            sum_embeddings = mx.sum(token_embeddings * attention_mask, axis=1)
            sum_mask = mx.sum(attention_mask, axis=1)
            embeddings = sum_embeddings / sum_mask
        else:
            # Default to first token if strategy is unknown
            embeddings = outputs.last_hidden_state[:, 0]

        # Normalize if needed
        if self.normalize:
            norms = mx.linalg.norm(embeddings, axis=1, keepdims=True)
            embeddings = embeddings / norms

        # Convert to numpy
        return [np.array(emb) for emb in embeddings]


class Embeddings:
    """
    Main class for generating embeddings using MLX.

    This class provides a high-level interface for loading and using
    embedding models with MLX.
    """

    def __init__(
        self,
        model_id: str = "mock",
        revision: Optional[str] = None,
        cache_dir: Optional[str] = None,
        use_fp16: bool = True,
        normalize: bool = True,
        pooling_strategy: str = "mean",
        max_length: Optional[int] = None,
        device: Optional[str] = None,
    ):
        """
        Initialize an Embeddings instance.

        Args:
            model_id: Model identifier (can be a HF model ID, local path, or "mock")
            revision: Model revision
            cache_dir: Cache directory for models
            use_fp16: Whether to use FP16 precision
            normalize: Whether to normalize embeddings to unit length
            pooling_strategy: Strategy for pooling token embeddings
            max_length: Maximum sequence length for tokenization
            device: Device to use (cpu, gpu, mps, etc.)
        """
        self.model_id = model_id
        self.revision = revision
        self.cache_dir = cache_dir
        self.use_fp16 = use_fp16
        self.normalize = normalize
        self.pooling_strategy = pooling_strategy
        self.max_length = max_length

        # Set device if specified
        if device:
            os.environ["LLAMAMLX_DEVICE"] = device

        # Set from environment if not specified
        self.device = device or os.environ.get("LLAMAMLX_DEVICE")

        # Initialize model path and embedding size
        self.model_path = None
        self.embedding_size = None

        # Initialize model
        self.model = self._load_model()

    def _load_model(self) -> EmbeddingModel:
        """
        Load the embedding model.

        Returns:
            Loaded embedding model

        Raises:
            ValueError: If model loading fails
        """
        # Special case for mock model
        if self.model_id.lower() == "mock":
            logger.info("Loading mock embedding model")
            from .mock_embeddings import MockEmbedding

            # Get embedding size from environment or use default
            embedding_size = int(os.environ.get("LLAMAMLX_EMBEDDING_SIZE", "768"))

            return MockEmbedding(
                embedding_size=embedding_size,
                model_id="mock-embedding",
            )

        try:
            # Get model information if available
            model_info = get_model_info(self.model_id)

            # Set embedding size if available in model info
            if model_info and "dim" in model_info:
                self.embedding_size = model_info["dim"]

            # Get model path (downloading if necessary)
            self.model_path = get_model_path(self.model_id, self.revision)

            # Load MLX model and tokenizer
            mlx_model, tokenizer = load_mlx_model(
                self.model_id,
                quantize=False,  # Handled separately
                model_type="dense",  # Default to dense
            )

            # Determine embedding size if not already set
            if self.embedding_size is None:
                # Try to get from model config
                if hasattr(mlx_model, "config") and hasattr(mlx_model.config, "hidden_size"):
                    self.embedding_size = mlx_model.config.hidden_size
                else:
                    # Default value
                    self.embedding_size = 768
                    logger.warning(
                        f"Could not determine embedding size, using default: {self.embedding_size}"
                    )

            # Create MLX embedding model
            return MLXEmbeddingModel(
                model_id=self.model_id,
                model=mlx_model,
                tokenizer=tokenizer,
                embedding_size=self.embedding_size,
                normalize=self.normalize,
                pooling_strategy=self.pooling_strategy,
                max_length=self.max_length,
            )

        except Exception as e:
            error_msg = f"Error loading model {self.model_id}: {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg) from e

    def encode(self, texts: Union[str, List[str]]) -> Union[np.ndarray, List[np.ndarray]]:
        """
        Encode text(s) into embeddings.

        Args:
            texts: Text or list of texts to encode

        Returns:
            Embedding vector(s)
        """
        return self.model.encode(texts)

    def encode_query(self, text: str) -> np.ndarray:
        """
        Encode a query text into an embedding.

        Args:
            text: Query text to encode

        Returns:
            Query embedding vector
        """
        return self.model.encode_query(text)

    def encode_documents(self, texts: List[str]) -> List[np.ndarray]:
        """
        Encode document texts into embeddings.

        Args:
            texts: List of document texts to encode

        Returns:
            List of document embedding vectors
        """
        return self.model.encode_documents(texts)

    def rerank(self, query: str, documents: List[str]) -> List[float]:
        """
        Rerank documents based on relevance to query.

        Args:
            query: Query text
            documents: List of document texts to rerank

        Returns:
            List of relevance scores (0-1) for each document
        """
        return self.model.rerank(query, documents)
