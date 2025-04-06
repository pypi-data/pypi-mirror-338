"""
Benchmark utilities for measuring performance of embedding models.
"""

import gc
import json
import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import mlx.core as mx
import numpy as np
import pandas as pd
import torch

from ..core.embeddings import EmbeddingModel

# Configure logging
logger = logging.getLogger(__name__)


@dataclass
class BenchmarkResult:
    """Benchmark result container."""

    model_name: str
    device: str
    batch_size: int
    sequence_length: int
    throughput: float  # tokens/second
    latency_mean: float  # ms
    latency_p50: float  # ms
    latency_p90: float  # ms
    latency_p99: float  # ms
    memory_usage: float  # MB
    batch_times: List[float]  # seconds

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "model_name": self.model_name,
            "device": self.device,
            "batch_size": self.batch_size,
            "sequence_length": self.sequence_length,
            "throughput": self.throughput,
            "latency_mean": self.latency_mean,
            "latency_p50": self.latency_p50,
            "latency_p90": self.latency_p90,
            "latency_p99": self.latency_p99,
            "memory_usage": self.memory_usage,
        }

    def __str__(self) -> str:
        """String representation."""
        return (
            f"BenchmarkResult(model={self.model_name}, device={self.device}, "
            f"batch_size={self.batch_size}, seq_len={self.sequence_length}, "
            f"throughput={self.throughput:.2f} tokens/s, "
            f"latency_mean={self.latency_mean:.2f}ms, "
            f"latency_p50={self.latency_p50:.2f}ms, "
            f"latency_p90={self.latency_p90:.2f}ms, "
            f"latency_p99={self.latency_p99:.2f}ms, "
            f"memory={self.memory_usage:.2f}MB)"
        )


def generate_random_text(n_samples: int, mean_len: int = 100, std_len: int = 20) -> List[str]:
    """
    Generate random text samples for benchmarking.

    Args:
        n_samples: Number of samples to generate
        mean_len: Mean length of samples in words
        std_len: Standard deviation of sample length

    Returns:
        List of text samples
    """
    words = [
        "the",
        "be",
        "to",
        "of",
        "and",
        "a",
        "in",
        "that",
        "have",
        "I",
        "it",
        "for",
        "not",
        "on",
        "with",
        "he",
        "as",
        "you",
        "do",
        "at",
        "this",
        "but",
        "his",
        "by",
        "from",
        "they",
        "we",
        "say",
        "her",
        "she",
        "or",
        "an",
        "will",
        "my",
        "one",
        "all",
        "would",
        "there",
        "their",
        "what",
        "so",
        "up",
        "out",
        "if",
        "about",
        "who",
        "get",
        "which",
        "go",
        "me",
        "document",
        "query",
        "search",
        "embedding",
        "vector",
        "model",
        "neural",
        "transformer",
        "language",
        "semantic",
        "similarity",
        "database",
        "retrieval",
        "machine",
        "learning",
        "artificial",
        "intelligence",
        "algorithm",
        "processing",
    ]

    result = []
    for _ in range(n_samples):
        # Sample length from normal distribution and clip to reasonable range
        length = int(np.random.normal(mean_len, std_len))
        length = max(10, min(length, 500))

        # Generate random text
        sample = " ".join(np.random.choice(words, size=length))
        result.append(sample)

    return result


def benchmark_model(
    model: EmbeddingModel,
    batch_sizes: List[int] = [1, 8, 32, 64, 128],
    n_samples: int = 100,
    warmup_iterations: int = 10,
    output_file: Optional[str] = None,
) -> Dict[int, BenchmarkResult]:
    """
    Benchmark an embedding model with different batch sizes.

    Args:
        model: Embedding model to benchmark
        batch_sizes: List of batch sizes to test
        n_samples: Number of samples to generate
        warmup_iterations: Number of warmup iterations
        output_file: Path to save benchmark results as JSON

    Returns:
        Dictionary mapping batch size to benchmark result
    """
    logger.info(f"Benchmarking model {model.model_id}")

    # Generate random text samples
    texts = generate_random_text(n_samples)

    # Get device info
    try:
        import platform

        device = f"{platform.system()}-{platform.processor()}"
        if hasattr(mx, "get_device") and mx.get_device() is not None:
            device += f"-{mx.get_device()}"
    except:
        device = "unknown"

    results = {}

    for batch_size in batch_sizes:
        logger.info(f"Testing batch size {batch_size}")

        # Skip if batch size is larger than number of samples
        if batch_size > n_samples:
            logger.warning(f"Skipping batch size {batch_size} as it exceeds number of samples")
            continue

        # Prepare batches
        num_batches = n_samples // batch_size
        batches = [texts[i * batch_size : (i + 1) * batch_size] for i in range(num_batches)]

        # Warmup
        logger.info(f"Warming up with {warmup_iterations} iterations")
        for _ in range(warmup_iterations):
            model.encode(batches[0])

        # Clear cache
        gc.collect()
        if hasattr(mx, "clear_memory"):
            mx.clear_memory()
        if hasattr(torch, "cuda") and torch.cuda.is_available():
            torch.cuda.empty_cache()

        # Benchmark
        logger.info(f"Running benchmark with {num_batches} batches")
        batch_times = []
        total_tokens = 0

        try:
            memory_before = get_memory_usage()
        except:
            memory_before = 0

        for batch in batches:
            # Time the embedding
            start_time = time.time()
            embeddings = model.encode(batch)
            mx.eval(embeddings)  # Force evaluation for MLX
            end_time = time.time()

            batch_time = end_time - start_time
            batch_times.append(batch_time)

            # Count tokens
            if hasattr(model, "tokenizer"):
                tokens = model.tokenizer(batch, padding=True, truncation=True)
                total_tokens += sum(len(ids) for ids in tokens["input_ids"])
            else:
                # Estimate tokens as words
                total_tokens += sum(len(text.split()) for text in batch)

        try:
            memory_after = get_memory_usage()
            memory_usage = memory_after - memory_before
        except:
            memory_usage = 0

        # Calculate metrics
        batch_times_ms = [t * 1000 for t in batch_times]
        latency_mean = np.mean(batch_times_ms)
        latency_p50 = np.percentile(batch_times_ms, 50)
        latency_p90 = np.percentile(batch_times_ms, 90)
        latency_p99 = np.percentile(batch_times_ms, 99)

        throughput = total_tokens / sum(batch_times)

        # Average sequence length
        sequence_length = total_tokens // (num_batches * batch_size)

        # Create result
        result = BenchmarkResult(
            model_name=model.model_id,
            device=device,
            batch_size=batch_size,
            sequence_length=sequence_length,
            throughput=throughput,
            latency_mean=latency_mean,
            latency_p50=latency_p50,
            latency_p90=latency_p90,
            latency_p99=latency_p99,
            memory_usage=memory_usage,
            batch_times=batch_times,
        )

        logger.info(str(result))
        results[batch_size] = result

    # Save results if output file specified
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        results_dict = {str(k): v.to_dict() for k, v in results.items()}
        with open(output_path, "w") as f:
            json.dump(results_dict, f, indent=2)

        logger.info(f"Saved benchmark results to {output_path}")

    return results


def compare_models(
    model_results: Dict[str, Dict[int, BenchmarkResult]],
    output_file: Optional[str] = None,
) -> pd.DataFrame:
    """
    Compare benchmark results from multiple models.

    Args:
        model_results: Dictionary mapping model name to benchmark results
        output_file: Path to save comparison results as CSV

    Returns:
        DataFrame with comparison results
    """
    records = []

    for model_name, results in model_results.items():
        for batch_size, result in results.items():
            records.append(
                {
                    "model": model_name,
                    "device": result.device,
                    "batch_size": batch_size,
                    "sequence_length": result.sequence_length,
                    "throughput": result.throughput,
                    "latency_mean": result.latency_mean,
                    "latency_p50": result.latency_p50,
                    "latency_p90": result.latency_p90,
                    "latency_p99": result.latency_p99,
                    "memory_usage": result.memory_usage,
                }
            )

    df = pd.DataFrame(records)

    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"Saved comparison results to {output_path}")

    return df


def get_memory_usage() -> float:
    """
    Get current memory usage in MB.

    Returns:
        Memory usage in MB
    """
    try:
        import psutil

        process = psutil.Process()
        memory_info = process.memory_info()
        return memory_info.rss / (1024 * 1024)  # Convert to MB
    except:
        return 0
