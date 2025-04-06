"""
ONNX-based embedding implementation for non-Apple hardware.
"""

import logging
import os
from typing import Iterable, List, Optional, Union

import numpy as np

# Use the new error handling utilities
from ..utils.error_handling import safe_import, require_dependency

# Handle onnxruntime import with better error messages
try:
    onnxruntime = safe_import("onnxruntime", extra_name="onnx")
    if onnxruntime:
        from onnxruntime import InferenceSession, SessionOptions
        ONNX_AVAILABLE = True
    else:
        ONNX_AVAILABLE = False
        # Define dummy classes to avoid errors when importing this module
        class InferenceSession:
            pass
        class SessionOptions:
            pass
except ImportError:
    logging.warning(
        "onnxruntime is not installed. ONNX embedding support is disabled. "
        "Install with: pip install onnxruntime or pip install llamamlx-embeddings[onnx]"
    )
    ONNX_AVAILABLE = False
    # Define dummy classes to avoid errors when importing this module
    class InferenceSession:
        pass
    class SessionOptions:
        pass

from transformers import AutoTokenizer

from .embeddings import BaseEmbedding, iter_batch
from .models import get_model_info

# Configure logging
logger = logging.getLogger(__name__)


def normalize(input_array: np.ndarray) -> np.ndarray:
    """
    Normalize vectors to unit length (NumPy version).

    Args:
        input_array: Input ndarray

    Returns:
        Normalized ndarray
    """
    norm = np.linalg.norm(input_array, axis=-1, keepdims=True)
    return input_array / (norm + 1e-12)


def mean_pooling(
    input_array: np.ndarray, attention_mask: Optional[np.ndarray] = None
) -> np.ndarray:
    """
    Compute mean pooling over token dimension (NumPy version).

    Args:
        input_array: Input tensor of shape [batch_size, seq_len, hidden_size]
        attention_mask: Optional attention mask to use for weighted pooling

    Returns:
        Mean pooled tensor of shape [batch_size, hidden_size]
    """
    if attention_mask is not None:
        # Weighted pooling based on attention mask
        input_array = input_array * attention_mask.reshape(
            attention_mask.shape[0], attention_mask.shape[1], 1
        )
        return np.sum(input_array, axis=1) / np.sum(attention_mask, axis=1, keepdims=True)
    else:
        # Simple mean pooling
        return np.mean(input_array, axis=1)


class OnnxTextEmbedding(BaseEmbedding):
    """
    Embeddings using ONNX Runtime. Provides CPU and GPU (CUDA) support.
    This is a fallback for when MLX is not available/suitable.
    """

    def load_model(self):
        """Loads the ONNX model and tokenizer."""
        if not ONNX_AVAILABLE:
            raise ImportError(
                "onnxruntime is required for OnnxTextEmbedding. "
                "Install with `pip install onnxruntime` or "
                "`pip install onnxruntime-gpu` for GPU support."
            )

        model_info = get_model_info(self.model_name)
        if model_info is None:
            raise ValueError(f"Model '{self.model_name}' is not supported.")

        try:
            # Try to get ONNX model and tokenizer from Hugging Face Hub
            from huggingface_hub import hf_hub_download

            logger.info(f"Downloading ONNX model for {self.model_name}")

            # Try common ONNX paths in model repositories
            try:
                model_path = hf_hub_download(
                    repo_id=self.model_name,
                    filename="onnx/model.onnx",
                    repo_type="model",
                    cache_dir=self.cache_dir,
                )
            except Exception:
                try:
                    # Try alternative path
                    model_path = hf_hub_download(
                        repo_id=self.model_name,
                        filename="model.onnx",
                        repo_type="model",
                        cache_dir=self.cache_dir,
                    )
                except Exception as e:
                    raise ValueError(
                        f"Could not find ONNX model for {self.model_name}. " f"Error: {str(e)}"
                    )

            # Load tokenizer
            logger.info(f"Loading tokenizer for {self.model_name}")
            self._tokenizer = AutoTokenizer.from_pretrained(
                self.model_name, cache_dir=self.cache_dir
            )

            # Configure and load ONNX session
            options = SessionOptions()
            options.intra_op_num_threads = os.cpu_count()  # Set CPU threads

            # Get providers from kwargs or use default
            providers = self.kwargs.get("providers", ["CPUExecutionProvider"])

            logger.info(f"Loading ONNX model with providers: {providers}")
            self._model = InferenceSession(model_path, options, providers=providers)

            # Log model metadata
            input_names = [x.name for x in self._model.get_inputs()]
            output_names = [x.name for x in self._model.get_outputs()]
            logger.info(f"ONNX model loaded with inputs: {input_names}, outputs: {output_names}")

        except Exception as e:
            logger.error(f"Error loading ONNX model: {str(e)}")
            raise

    def embed(
        self,
        inputs: Union[str, List[str], Iterable[str]],
        batch_size: int = 32,
        **kwargs,
    ) -> Iterable[List[List[float]]]:
        """
        Generate embeddings using ONNX model.

        Args:
            inputs: Input text or list of texts
            batch_size: Batch size for processing
            **kwargs: Additional arguments

        Yields:
            Embeddings for each input or batch as List[List[float]]
        """
        inputs = self._process_input(inputs)

        try:
            for batch in iter_batch(inputs, batch_size):
                # Handle query/passage prefixes (same logic as TextEmbedding)
                prefixed_batch = []
                for text in batch:
                    if text.startswith("query:") or text.startswith("passage:"):
                        prefixed_batch.append(text)  # Already prefixed
                    elif self.model_name.startswith("BAAI/bge") or self.model_name.startswith(
                        "intfloat/e5"
                    ):
                        if kwargs.get("is_passage", True):
                            prefixed_batch.append("passage: " + text)
                        else:
                            prefixed_batch.append("query: " + text)
                    else:
                        prefixed_batch.append(text)

                # Tokenize inputs
                max_length = kwargs.get("max_length", 512)
                inputs_encoded = self._tokenizer(
                    prefixed_batch,
                    padding=True,
                    truncation=True,
                    return_tensors="np",
                    max_length=max_length,
                )

                # Prepare ONNX input
                model_inputs = {
                    k: v
                    for k, v in inputs_encoded.items()
                    if k in [x.name for x in self._model.get_inputs()]
                }

                # Run inference
                outputs = self._model.run(None, model_inputs)

                # Process outputs based on model type
                if len(outputs) > 0:
                    # For most models, the first output is the embeddings
                    embeddings = outputs[0]

                    # Apply mean pooling if needed (depends on model architecture)
                    if len(embeddings.shape) == 3:  # [batch_size, seq_len, hidden_dim]
                        embeddings = mean_pooling(embeddings, inputs_encoded.get("attention_mask"))

                    # Normalize if requested
                    if self.normalize:
                        embeddings = normalize(embeddings)

                    yield embeddings.tolist()
                else:
                    raise ValueError("No outputs from ONNX model")

        except Exception as e:
            logger.error(f"Error generating embeddings with ONNX: {str(e)}")
            raise

    def embed_query(self, query: str, **kwargs) -> List[float]:
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

    def embed_documents(self, documents: List[str], **kwargs) -> List[List[float]]:
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
