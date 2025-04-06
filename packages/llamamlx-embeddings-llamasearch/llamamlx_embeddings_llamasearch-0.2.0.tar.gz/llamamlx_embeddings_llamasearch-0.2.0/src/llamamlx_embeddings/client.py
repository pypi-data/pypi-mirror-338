"""
Client for the llamamlx-embeddings API.
"""

import logging
from typing import Any, Dict, List, Optional, Union

import requests

# Configure logging
logger = logging.getLogger(__name__)


class LlamamlxEmbeddingsClient:
    """
    Client for interacting with the llamamlx-embeddings API.
    """

    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Initialize the client.

        Args:
            base_url: Base URL of the llamamlx-embeddings API
        """
        self.base_url = base_url.rstrip("/")
        logger.info(f"Initialized client with base URL: {self.base_url}")

    def _request(self, method: str, endpoint: str, data: Optional[dict] = None) -> dict:
        """
        Helper function to make requests to the API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            data: Request payload

        Returns:
            JSON response as dictionary

        Raises:
            RuntimeError: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"Making {method} request to {url}")

        try:
            if method.upper() == "GET":
                response = requests.get(url)
            else:
                response = requests.request(
                    method=method, url=url, json=data, headers={"Content-Type": "application/json"}
                )

            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()

        except requests.exceptions.RequestException as e:
            error_msg = f"API request failed: {e}"
            logger.error(error_msg)

            # Try to extract more details from the response if available
            if hasattr(e, "response") and e.response is not None:
                try:
                    error_details = e.response.json()
                    error_msg += f", Details: {error_details}"
                except:
                    if e.response.text:
                        error_msg += f", Response: {e.response.text}"

            raise RuntimeError(error_msg) from e

        except ValueError as e:
            # JSON decoding errors
            error_msg = f"Invalid JSON response from server: {e}"
            logger.error(error_msg)
            raise RuntimeError(error_msg) from e

    def get_embeddings(
        self,
        input_texts: Union[str, List[str]],
        model_name: str = "BAAI/bge-small-en-v1.5",
        quantize: bool = False,
        device: str = "auto",
        is_query: bool = False,
    ) -> List[List[float]]:
        """
        Get embeddings for input text(s) from the API.

        Args:
            input_texts: The input text or list of texts
            model_name: The name of the embedding model
            quantize: Use a quantized model or not
            device: 'auto', 'cpu', 'cuda', or 'mlx'
            is_query: Whether the input is a query (for query/passage models)

        Returns:
            A list of embeddings (list of floats)

        Raises:
            ValueError: If the server response format is invalid
            RuntimeError: If the API request fails
        """
        data = {
            "input": input_texts,
            "model_name": model_name,
            "quantize": quantize,
            "device": device,
            "is_query": is_query,
        }

        try:
            logger.info(f"Getting embeddings using model: {model_name}")
            response_data = self._request("POST", "/embeddings", data)

            # Basic validation of response format
            if "embeddings" not in response_data:
                raise ValueError("Missing 'embeddings' in server response")

            return response_data["embeddings"]

        except Exception as e:
            logger.error(f"Error getting embeddings: {str(e)}")
            raise

    def list_models(self) -> List[Dict[str, Any]]:
        """
        List available embedding models from the API.

        Returns:
            A list of model information dictionaries

        Raises:
            ValueError: If the server response format is invalid
            RuntimeError: If the API request fails
        """
        try:
            logger.info("Listing available models")
            response_data = self._request("GET", "/models")

            # Basic validation of response format
            if "models" not in response_data:
                raise ValueError("Missing 'models' in server response")

            return response_data["models"]

        except Exception as e:
            logger.error(f"Error listing models: {str(e)}")
            raise

    def rerank(
        self,
        query: str,
        documents: List[str],
        model_name: str = "Xenova/ms-marco-MiniLM-L-6-v2",
        device: str = "auto",
    ) -> List[float]:
        """
        Rerank documents using a cross-encoder via the API.

        Args:
            query: The query text
            documents: The list of documents to rerank
            model_name: The cross-encoder model name
            device: 'auto', 'cpu', 'cuda', or 'mlx'

        Returns:
            A list of reranking scores

        Raises:
            ValueError: If the server response format is invalid
            RuntimeError: If the API request fails
        """
        data = {"query": query, "documents": documents, "model_name": model_name, "device": device}

        try:
            logger.info(f"Reranking {len(documents)} documents using model: {model_name}")
            response_data = self._request("POST", "/rerank", data)

            # Basic validation of response format
            if "scores" not in response_data:
                raise ValueError("Missing 'scores' in server response")

            return response_data["scores"]

        except Exception as e:
            logger.error(f"Error reranking documents: {str(e)}")
            raise

    def health_check(self) -> Dict[str, Any]:
        """
        Check the health status of the API.

        Returns:
            Dictionary with health status information

        Raises:
            RuntimeError: If the API request fails
        """
        try:
            logger.info("Checking API health")
            return self._request("GET", "/health")

        except Exception as e:
            logger.error(f"Error checking API health: {str(e)}")
            raise
