#!/usr/bin/env python
"""
Comprehensive benchmarking tool for llamamlx-embeddings.

This script runs performance benchmarks for different embedding models and configurations,
comparing MLX implementations with ONNX and alternatives like sentence-transformers.
"""

import argparse
import datetime
import json
import os
import platform
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
import psutil

# Add parent directory to system path for local imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from llamamlx_embeddings import (
    TextEmbedding,
    configure_logging,
    get_logger,
    list_supported_models,
)

# Configure logging
configure_logging(level="INFO")
logger = get_logger("benchmarks.run")


def get_system_info() -> Dict[str, Any]:
    """Collect system information for benchmarking context."""
    system_info = {
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "processor": platform.processor(),
        "architecture": platform.machine(),
        "cpu_count": psutil.cpu_count(logical=False),
        "logical_cpus": psutil.cpu_count(logical=True),
        "memory_gb": round(psutil.virtual_memory().total / (1024**3), 2),
    }

    # Try to get Apple Silicon details if available
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        # Try to determine specific Apple Silicon chip
        try:
            import subprocess

            result = subprocess.run(
                ["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True
            )
            system_info["apple_silicon"] = result.stdout.strip()
        except Exception:
            system_info["apple_silicon"] = "Apple Silicon (unknown model)"

    # Check for GPU if possible
    try:
        # For CUDA
        import torch

        system_info["cuda_available"] = torch.cuda.is_available()
        if torch.cuda.is_available():
            system_info["cuda_device"] = torch.cuda.get_device_name(0)
            system_info["cuda_version"] = torch.version.cuda
    except ImportError:
        system_info["cuda_available"] = False

    return system_info


def generate_texts(num_texts: int = 100, min_words: int = 20, max_words: int = 200) -> List[str]:
    """Generate synthetic texts for benchmarking."""
    # Use a fixed seed for reproducibility
    np.random.seed(42)

    # Define a vocabulary of common words
    vocab = [
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
        "when",
        "make",
        "can",
        "like",
        "time",
        "no",
        "just",
        "him",
        "know",
        "take",
        "person",
        "into",
        "year",
        "your",
        "good",
        "some",
        "could",
        "them",
        "see",
        "other",
        "than",
        "then",
        "now",
        "look",
        "only",
        "come",
        "its",
        "over",
        "think",
        "also",
        "back",
        "after",
        "use",
        "two",
        "how",
        "our",
        "work",
        "first",
        "well",
        "way",
        "even",
        "new",
        "want",
        "because",
        "any",
        "these",
        "give",
        "day",
        "most",
        "us",
        "machine",
        "learning",
        "artificial",
        "intelligence",
        "data",
        "model",
        "training",
        "neural",
        "network",
        "deep",
        "embeddings",
        "vector",
        "semantic",
        "search",
        "similarity",
        "transformer",
        "attention",
        "bert",
        "language",
        "llm",
        "generation",
        "fine-tuning",
        "hyperparameter",
        "optimization",
        "loss",
        "function",
        "gradient",
        "descent",
        "backpropagation",
    ]

    # Generate random texts
    texts = []
    for _ in range(num_texts):
        num_words = np.random.randint(min_words, max_words + 1)
        words = np.random.choice(vocab, size=num_words).tolist()
        text = " ".join(words)
        texts.append(text)

    return texts


def time_execution(
    func: Callable, *args, num_runs: int = 3, warmup_runs: int = 1, **kwargs
) -> Dict[str, float]:
    """
    Time the execution of a function with warmup runs.

    Args:
        func: Function to time
        *args: Arguments to pass to the function
        num_runs: Number of timing runs to perform
        warmup_runs: Number of warmup runs to perform
        **kwargs: Keyword arguments to pass to the function

    Returns:
        Dictionary with timing statistics
    """
    # Perform warmup runs (not timed)
    for _ in range(warmup_runs):
        func(*args, **kwargs)

    # Perform timed runs
    run_times = []
    for _ in range(num_runs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_times.append(end_time - start_time)

    # Calculate statistics
    run_times = np.array(run_times)
    stats = {
        "mean": float(np.mean(run_times)),
        "min": float(np.min(run_times)),
        "max": float(np.max(run_times)),
        "median": float(np.median(run_times)),
        "std": float(np.std(run_times)),
        "runs": run_times.tolist(),
    }

    return stats


def benchmark_model(
    model_name: str,
    texts: List[str],
    batch_sizes: List[int],
    num_runs: int = 3,
    warmup_runs: int = 1,
    quantize: bool = False,
) -> Dict[str, Any]:
    """
    Benchmark a single model with different batch sizes.

    Args:
        model_name: Name of the model to benchmark
        texts: List of texts to embed
        batch_sizes: List of batch sizes to test
        num_runs: Number of runs to perform for each configuration
        warmup_runs: Number of warmup runs to perform
        quantize: Whether to use quantized model

    Returns:
        Dictionary with benchmark results
    """
    results = {
        "model_name": model_name,
        "num_texts": len(texts),
        "quantize": quantize,
        "batch_results": {},
    }

    try:
        # Load model
        logger.info(f"Loading model {model_name} (quantize={quantize})...")
        model = TextEmbedding(model_name=model_name, quantize=quantize)

        # Get model info
        embed_dim = len(model.embed_query("Test query"))
        results["embed_dim"] = embed_dim

        # Test each batch size
        for batch_size in batch_sizes:
            logger.info(f"Testing batch_size={batch_size}...")

            # Time embedding with this batch size
            timing = time_execution(
                model.embed_documents,
                texts,
                batch_size=batch_size,
                num_runs=num_runs,
                warmup_runs=warmup_runs,
            )

            # Calculate performance metrics
            throughput = len(texts) / timing["mean"]  # texts per second

            results["batch_results"][str(batch_size)] = {
                "timing": timing,
                "throughput": throughput,
            }

            logger.info(f"  Throughput: {throughput:.2f} texts/sec")

    except Exception as e:
        logger.error(f"Error benchmarking {model_name}: {str(e)}")
        results["error"] = str(e)

    return results


def run_benchmarks(
    model_names: List[str],
    batch_sizes: List[int],
    num_texts: int = 100,
    text_length: Tuple[int, int] = (50, 200),
    num_runs: int = 3,
    warmup_runs: int = 1,
    include_quantized: bool = True,
    output_file: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Run benchmarks for multiple models and configurations.

    Args:
        model_names: List of model names to benchmark
        batch_sizes: List of batch sizes to test
        num_texts: Number of texts to generate for testing
        text_length: Tuple of (min_words, max_words) for text generation
        num_runs: Number of runs for each configuration
        warmup_runs: Number of warmup runs
        include_quantized: Whether to include quantized models
        output_file: Path to save results as JSON (if provided)

    Returns:
        Dictionary with all benchmark results
    """
    # Record start time
    start_time = datetime.datetime.now()

    # Collect system information
    system_info = get_system_info()
    logger.info(
        f"System: {system_info['platform']} - {system_info.get('apple_silicon', system_info['processor'])}"
    )

    # Generate texts for benchmarking
    logger.info(
        f"Generating {num_texts} texts with length {text_length[0]}-{text_length[1]} words..."
    )
    texts = generate_texts(num_texts, text_length[0], text_length[1])

    # Initialize results
    results = {
        "timestamp": start_time.isoformat(),
        "system_info": system_info,
        "config": {
            "num_texts": num_texts,
            "text_length": text_length,
            "num_runs": num_runs,
            "warmup_runs": warmup_runs,
            "include_quantized": include_quantized,
            "batch_sizes": batch_sizes,
        },
        "models": {},
    }

    # Benchmark each model
    for model_name in model_names:
        logger.info(f"\nBenchmarking model: {model_name}")

        # Standard model
        model_results = benchmark_model(
            model_name=model_name,
            texts=texts,
            batch_sizes=batch_sizes,
            num_runs=num_runs,
            warmup_runs=warmup_runs,
            quantize=False,
        )
        results["models"][f"{model_name}"] = model_results

        # Quantized model if requested
        if include_quantized:
            model_results_q = benchmark_model(
                model_name=model_name,
                texts=texts,
                batch_sizes=batch_sizes,
                num_runs=num_runs,
                warmup_runs=warmup_runs,
                quantize=True,
            )
            results["models"][f"{model_name}_quantized"] = model_results_q

    # Record end time and duration
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()
    results["duration_seconds"] = duration

    logger.info(f"\nBenchmarking completed in {duration:.2f} seconds")

    # Save results if output file provided
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(results, f, indent=2)

        logger.info(f"Results saved to {output_path}")

    return results


def print_summary(results: Dict[str, Any]) -> None:
    """Print a summary of benchmark results."""
    print("\n" + "=" * 80)
    print(f"BENCHMARK SUMMARY - {results['timestamp']}")
    print("=" * 80)

    print(f"\nSystem: {results['system_info']['platform']}")
    if "apple_silicon" in results["system_info"]:
        print(f"Processor: {results['system_info']['apple_silicon']}")
    else:
        print(f"Processor: {results['system_info']['processor']}")

    print(f"Python: {results['system_info']['python_version']}")
    print(f"Memory: {results['system_info']['memory_gb']} GB")

    print("\nModel Throughput (texts/second):")
    print("-" * 80)
    print(f"{'Model':40} {'Dimension':10}", end="")

    # Print batch size headers
    batch_sizes = [int(bs) for bs in results["config"]["batch_sizes"]]
    for bs in batch_sizes:
        print(f" {'BS='+str(bs):10}", end="")
    print()
    print("-" * 80)

    # Print results for each model
    for model_name, model_data in results["models"].items():
        if "error" in model_data:
            print(f"{model_name:40} ERROR: {model_data['error']}")
            continue

        dim = model_data.get("embed_dim", "N/A")
        print(f"{model_name:40} {dim:<10}", end="")

        for bs in batch_sizes:
            bs_str = str(bs)
            if bs_str in model_data["batch_results"]:
                throughput = model_data["batch_results"][bs_str]["throughput"]
                print(f" {throughput:10.2f}", end="")
            else:
                print(f" {'N/A':10}", end="")
        print()

    print("-" * 80)
    print(f"Total benchmark duration: {results['duration_seconds']:.2f} seconds")
    print("=" * 80)


def main():
    """Main entry point for the benchmarking script."""
    parser = argparse.ArgumentParser(description="Run benchmarks for llamamlx-embeddings")
    parser.add_argument(
        "--models",
        nargs="+",
        default=["BAAI/bge-small-en-v1.5", "sentence-transformers/all-MiniLM-L6-v2"],
        help="Model(s) to benchmark",
    )
    parser.add_argument("--list-models", action="store_true", help="List available models and exit")
    parser.add_argument(
        "--batch-sizes", nargs="+", type=int, default=[1, 8, 32], help="Batch size(s) to test"
    )
    parser.add_argument(
        "--num-texts", type=int, default=100, help="Number of texts to benchmark with"
    )
    parser.add_argument("--min-words", type=int, default=50, help="Minimum words per text")
    parser.add_argument("--max-words", type=int, default=200, help="Maximum words per text")
    parser.add_argument("--runs", type=int, default=3, help="Number of runs per configuration")
    parser.add_argument("--warmup", type=int, default=1, help="Number of warmup runs")
    parser.add_argument(
        "--no-quantized", action="store_true", help="Skip quantized model benchmarks"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="benchmark_results.json",
        help="Output file for results (JSON format)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    # Configure logging level
    if args.verbose:
        configure_logging(level="DEBUG")

    # List models and exit if requested
    if args.list_models:
        models = list_supported_models()
        print("\nAvailable Models:")
        print("-" * 80)
        print(f"{'Model Name':60} {'Type':15} {'Dimensions':10}")
        print("-" * 80)
        for model in models:
            print(f"{model['model']:60} {model['model_type']:15} {model['dim']:10}")
        print("-" * 80)
        return 0

    # Run benchmarks
    results = run_benchmarks(
        model_names=args.models,
        batch_sizes=args.batch_sizes,
        num_texts=args.num_texts,
        text_length=(args.min_words, args.max_words),
        num_runs=args.runs,
        warmup_runs=args.warmup,
        include_quantized=not args.no_quantized,
        output_file=args.output,
    )

    # Print summary
    print_summary(results)

    return 0


if __name__ == "__main__":
    sys.exit(main())
