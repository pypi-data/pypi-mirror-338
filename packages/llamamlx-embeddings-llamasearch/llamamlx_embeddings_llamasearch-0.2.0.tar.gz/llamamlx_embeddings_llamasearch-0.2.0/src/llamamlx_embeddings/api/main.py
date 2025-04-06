"""
FastAPI server for serving embeddings through a REST API.
"""

import logging
from typing import List, Optional, Union

import mlx.core as mx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel, Field, validator

from .. import __version__
from ..core.embeddings import (
    LateInteractionTextEmbedding,
    SparseTextEmbedding,
    TextCrossEncoder,
    TextEmbedding,
)
from ..core.models import get_model_info, list_supported_models
from ..core.onnx_embedding import OnnxTextEmbedding  # For CPU/GPU fallback

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="llamamlx-embeddings API",
    description="A high-performance embedding service built with MLX.",
    version=__version__,
)

# Add GZip compression middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Global cache for loaded models to avoid reloading on each request
MODEL_CACHE = {}


# --- Pydantic Models ---
class EmbeddingRequest(BaseModel):
    """Request for generating embeddings."""

    input: Union[str, List[str]] = Field(..., description="Input text or list of texts to embed.")
    model_name: str = Field(
        "BAAI/bge-small-en-v1.5", description="Name of the embedding model to use."
    )
    quantize: bool = Field(False, description="Whether to use a quantized model.")
    device: str = Field(
        "auto",
        description="Device to use ('auto', 'cpu', 'cuda'). 'auto' prioritizes MLX, then CUDA, then CPU.",
    )
    is_query: bool = Field(
        False,
        description="Whether the input is a query (for models that handle queries and passages differently).",
    )

    @validator("device")
    def validate_device(cls, v):
        allowed_devices = ["auto", "cpu", "cuda", "mlx"]
        if v not in allowed_devices:
            raise ValueError(f"Device must be one of {allowed_devices}")
        return v


class EmbeddingResponse(BaseModel):
    """Response containing embeddings."""

    embeddings: List[List[float]]
    model_name: str
    device: str


class ModelInfo(BaseModel):
    """Information about an embedding model."""

    model_name: str
    model_type: str  # e.g., "dense", "sparse", "late_interaction"
    dimensions: int
    description: Optional[str] = None


class ModelListResponse(BaseModel):
    """Response listing available models."""

    models: List[ModelInfo]


class RerankRequest(BaseModel):
    """Request for reranking documents."""

    query: str = Field(..., description="The query text.")
    documents: List[str] = Field(..., description="List of documents to rerank.")
    model_name: str = Field(
        "Xenova/ms-marco-MiniLM-L-6-v2", description="Cross-encoder model name."
    )
    device: str = Field("auto", description="Device: 'auto', 'cpu', 'cuda'.")

    @validator("device")
    def validate_device(cls, v):
        allowed_devices = ["auto", "cpu", "cuda", "mlx"]
        if v not in allowed_devices:
            raise ValueError(f"Device must be one of {allowed_devices}")
        return v


class RerankResponse(BaseModel):
    """Response containing reranking scores."""

    scores: List[float] = Field(..., description="Reranking scores for each document.")
    model_name: str
    device: str


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = "OK"
    version: str = __version__
    available_devices: List[str]


# --- Helper Functions ---
def get_device(requested_device: str) -> str:
    """
    Determine the actual device to use based on the requested device.

    Args:
        requested_device: Requested device ('auto', 'cpu', 'cuda', 'mlx')

    Returns:
        The actual device to use
    """
    if requested_device == "auto":
        # Check if MLX is available and using GPU
        try:
            if mx.default_device() == mx.gpu:
                return "mlx"
            else:
                # MLX is available but using CPU
                try:
                    # Check if CUDA is available
                    import torch

                    if torch.cuda.is_available():
                        return "cuda"
                except ImportError:
                    pass
                # Fall back to CPU
                return "cpu"
        except:
            # MLX not available or error occurred, check for CUDA
            try:
                import torch

                if torch.cuda.is_available():
                    return "cuda"
            except ImportError:
                pass
            # Fall back to CPU
            return "cpu"
    else:
        # Use the explicitly requested device
        return requested_device


def get_embedding_model(model_name: str, device: str, quantize: bool = False):
    """
    Get an embedding model, using cached model if available.

    Args:
        model_name: Name of the model to load
        device: Device to use ('mlx', 'cpu', 'cuda')
        quantize: Whether to use a quantized model

    Returns:
        The loaded embedding model
    """
    # Create a cache key based on the parameters
    cache_key = f"{model_name}_{device}_{quantize}"

    # Return cached model if available
    if cache_key in MODEL_CACHE:
        logger.info(f"Using cached model for {cache_key}")
        return MODEL_CACHE[cache_key]

    # Otherwise, load the model
    logger.info(f"Loading model {model_name} on {device} (quantize={quantize})")

    try:
        model_info = get_model_info(model_name)
        if model_info is None:
            raise ValueError(f"Model '{model_name}' is not supported.")

        if device in ("cpu", "cuda"):
            # Use ONNX for CPU or CUDA
            providers = [f"{device.upper()}ExecutionProvider"]
            model = OnnxTextEmbedding(model_name=model_name, providers=providers)
        else:
            # Use MLX (Apple Silicon)
            if model_info["model_type"] == "dense":
                model = TextEmbedding(model_name=model_name, quantize=quantize)
            elif model_info["model_type"] == "sparse":
                model = SparseTextEmbedding(model_name=model_name)
            elif model_info["model_type"] == "late_interaction":
                model = LateInteractionTextEmbedding(model_name=model_name)
            else:
                raise ValueError(f"Unsupported model type: {model_info['model_type']}")

        # Cache the model for future use
        MODEL_CACHE[cache_key] = model
        return model

    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise


def get_cross_encoder_model(model_name: str, device: str):
    """
    Get a cross-encoder model, using cached model if available.

    Args:
        model_name: Name of the model to load
        device: Device to use ('mlx', 'cpu', 'cuda')

    Returns:
        The loaded cross-encoder model
    """
    # Create a cache key based on the parameters
    cache_key = f"cross_{model_name}_{device}"

    # Return cached model if available
    if cache_key in MODEL_CACHE:
        logger.info(f"Using cached cross-encoder for {cache_key}")
        return MODEL_CACHE[cache_key]

    # Otherwise, load the model
    logger.info(f"Loading cross-encoder {model_name} on {device}")

    try:
        if device in ("cpu", "cuda"):
            # Use an adapter class for ONNX cross-encoders (not implemented in this code)
            # This is a placeholder - full implementation would depend on specific needs
            raise NotImplementedError("ONNX cross-encoders not yet implemented. Use 'mlx' instead.")
        else:
            # Use MLX implementation
            model = TextCrossEncoder(model_name=model_name)

        # Cache the model for future use
        MODEL_CACHE[cache_key] = model
        return model

    except Exception as e:
        logger.error(f"Error loading cross-encoder: {str(e)}")
        raise


# --- API Endpoints ---
@app.post("/embeddings", response_model=EmbeddingResponse)
async def create_embeddings(request: EmbeddingRequest):
    """
    Generate embeddings for the input text or texts.

    Args:
        request: The request containing input text(s) and model parameters

    Returns:
        A response containing the generated embeddings
    """
    try:
        # Determine the device to use
        device = get_device(request.device)
        logger.info(f"Using device: {device}")

        # Get the model (cached or new)
        model = get_embedding_model(
            model_name=request.model_name, device=device, quantize=request.quantize
        )

        # Prepare inputs
        inputs = request.input
        is_query = request.is_query

        # Generate embeddings
        if isinstance(inputs, str):
            # Single input
            if is_query:
                emb = (
                    model.embed_query(inputs)
                    if hasattr(model, "embed_query")
                    else next(model.embed(inputs))
                )
                embeddings = [emb.tolist()]  # Single embedding
            else:
                emb = next(model.embed(inputs))
                embeddings = [
                    emb.tolist() if hasattr(emb, "tolist") else emb
                ]  # Handle mx.array or list
        else:
            # Multiple inputs
            if hasattr(model, "embed_documents") and not is_query:
                # Use batch embedding for documents if available
                embs = model.embed_documents(inputs)
                embeddings = [e.tolist() if hasattr(e, "tolist") else e for e in embs]
            else:
                # Otherwise use the generic embed method
                embs = next(model.embed(inputs, is_query=is_query))
                embeddings = [e.tolist() if hasattr(e, "tolist") else e for e in embs]

        # Handle sparse embeddings differently if needed
        from ..core.sparse import SparseEmbedding

        if isinstance(embeddings[0], SparseEmbedding):
            # For sparse embeddings, just return the indices and values
            sparse_embeddings = []
            for emb in embeddings:
                sparse_embeddings.append({"indices": emb.indices, "values": emb.values})
            return {
                "embeddings": sparse_embeddings,
                "model_name": request.model_name,
                "device": device,
            }

        # Return the response
        return {"embeddings": embeddings, "model_name": request.model_name, "device": device}

    except Exception as e:
        logger.error(f"Error generating embeddings: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/models", response_model=ModelListResponse)
async def list_models():
    """
    List all available embedding models.

    Returns:
        A response containing a list of available models
    """
    try:
        models_list = list_supported_models()
        result = []

        for model_info in models_list:
            result.append(
                {
                    "model_name": model_info["model"],
                    "model_type": model_info["model_type"],
                    "dimensions": model_info["dim"],
                    "description": model_info.get("description", "No description"),
                }
            )

        return {"models": result}

    except Exception as e:
        logger.error(f"Error listing models: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rerank", response_model=RerankResponse)
async def rerank(request: RerankRequest):
    """
    Rerank documents based on their relevance to a query.

    Args:
        request: The request containing the query, documents, and model parameters

    Returns:
        A response containing reranking scores for each document
    """
    try:
        # Determine the device to use
        device = get_device(request.device)
        logger.info(f"Using device: {device}")

        # Get the cross-encoder model
        model = get_cross_encoder_model(model_name=request.model_name, device=device)

        # Get the reranking scores
        scores = model.rerank(request.query, request.documents)

        # Return the response
        return {"scores": scores, "model_name": request.model_name, "device": device}

    except Exception as e:
        logger.error(f"Error reranking documents: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Check the health of the API.

    Returns:
        A response containing health status information
    """
    available_devices = ["cpu"]

    # Check for MLX
    try:
        import mlx.core as mx

        if mx.default_device() == mx.gpu:
            available_devices.append("mlx")
    except:
        pass

    # Check for CUDA
    try:
        import torch

        if torch.cuda.is_available():
            available_devices.append("cuda")
    except:
        pass

    return {"status": "OK", "version": __version__, "available_devices": available_devices}
