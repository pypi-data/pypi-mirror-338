"""
Command-line interface for llamamlx-embeddings.
"""

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import List, Optional

import uvicorn

from . import __version__
from .core.models import list_supported_models
from .core.conversion import convert_hf_to_mlx, optimize_mlx_model
from .core.embeddings import TextEmbedding, SparseTextEmbedding, LateInteractionTextEmbedding
from .core.mock_embeddings import MockEmbedding
from .processing.text import chunk_text, preprocess_text

# Import benchmark module only when needed to avoid circular imports
# Will be imported in benchmark_command function

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger("llamamlx-cli")


def progress_callback(progress: float, message: str) -> None:
    """Print progress updates."""
    bar_length = 30
    filled_length = int(bar_length * progress)
    bar = "=" * filled_length + "-" * (bar_length - filled_length)
    sys.stdout.write(f"\r[{bar}] {progress:.1%} {message}")
    sys.stdout.flush()

    if progress >= 1.0:
        sys.stdout.write("\n")


def convert_command(args) -> None:
    """Convert a Hugging Face model to MLX format."""
    try:
        logger.info(f"Converting model {args.model_id} to MLX format")

        output_path = convert_hf_to_mlx(
            model_id=args.model_id,
            output_dir=args.output_dir,
            revision=args.revision,
            dtype=args.dtype,
            overwrite=args.overwrite,
        )

        if args.quantize:
            logger.info("Quantizing model weights")
            optimize_mlx_model(
                model_dir=output_path,
                quantize=True,
            )

        logger.info(f"Model converted successfully to {output_path}")

    except Exception as e:
        logger.error(f"Error converting model: {str(e)}")
        sys.exit(1)


def serve_command(args) -> None:
    """Start the API server."""
    try:
        # Import here to avoid circular imports
        from .api.main import app

        logger.info(f"Starting API server on {args.host}:{args.port}")

        # Set model settings to environment variables
        if args.model:
            os.environ["LLAMAMLX_MODEL"] = args.model
        if args.device:
            os.environ["LLAMAMLX_DEVICE"] = args.device
        if args.max_length:
            os.environ["LLAMAMLX_MAX_LENGTH"] = str(args.max_length)

        uvicorn.run(app, host=args.host, port=args.port, log_level=args.log_level.lower())

    except Exception as e:
        logger.error(f"Error starting API server: {str(e)}")
        sys.exit(1)


def list_models_command(args) -> None:
    """List supported models."""
    try:
        models = list_supported_models()

        print("Supported Models:")
        print("----------------")

        for category, model_list in models.items():
            print(f"\n{category}:")
            for model in model_list:
                print(f"  - {model}")

    except Exception as e:
        logger.error(f"Error listing models: {str(e)}")
        sys.exit(1)


def download_command(args) -> None:
    """Download a model."""
    try:
        logger.info(f"Downloading model {args.model_id}")

        embeddings = TextEmbedding(
            model_id=args.model_id,
            revision=args.revision,
            cache_dir=args.cache_dir,
            use_fp16=not args.no_fp16,
        )

        logger.info(f"Model {args.model_id} downloaded successfully")
        logger.info(f"Model path: {embeddings.model_path}")

    except Exception as e:
        logger.error(f"Error downloading model: {str(e)}")
        sys.exit(1)


def benchmark_command(args) -> None:
    """Run a benchmark on a specified model."""
    try:
        # Import here to avoid circular imports
        from .benchmarks.benchmark import benchmark_model
        
        if args.model_id == "mock":
            logger.info("Running benchmark with mock embedding model")
            model = MockEmbedding(embedding_size=args.embedding_size)
            
            # Convert batch sizes string to list of integers
            batch_sizes = [int(bs) for bs in args.batch_sizes.split(",")]
            
            results = benchmark_model(
                model=model,
                batch_sizes=batch_sizes,
                n_samples=args.n_samples,
                warmup_iterations=args.warmup,
                output_file=args.output,
            )
        else:
            logger.info(f"Benchmarking model {args.model_id}")
            
            embeddings = TextEmbedding(
                model_id=args.model_id,
                revision=args.revision,
                cache_dir=args.cache_dir,
                use_fp16=not args.no_fp16,
            )
            model = embeddings.model
            
            # Convert batch sizes string to list of integers
            batch_sizes = [int(bs) for bs in args.batch_sizes.split(",")]
            
            results = benchmark_model(
                model=model,
                batch_sizes=batch_sizes,
                n_samples=args.n_samples,
                warmup_iterations=args.warmup,
                output_file=args.output,
            )
            
            # Display summary
            print("\nBenchmark Summary:")
            print("----------------")
            
            for batch_size, result in results.items():
                print(f"\nBatch Size: {batch_size}")
                print(f"  Throughput: {result.throughput:.2f} tokens/s")
                print(f"  Mean Latency: {result.latency_mean:.2f} ms")
                print(f"  90th Percentile Latency: {result.latency_p90:.2f} ms")
                print(f"  Memory Usage: {result.memory_usage:.2f} MB")

    except Exception as e:
        logger.error(f"Error benchmarking model: {str(e)}")
        sys.exit(1)


def embed_command(args) -> None:
    """Embed texts."""
    try:
        if args.input_file:
            # Read from file
            with open(args.input_file, "r", encoding="utf-8") as f:
                if args.input_file.endswith(".json"):
                    data = json.load(f)
                    if isinstance(data, list):
                        texts = data
                    elif isinstance(data, dict) and "texts" in data:
                        texts = data["texts"]
                    else:
                        texts = [json.dumps(data)]
                else:
                    texts = [line.strip() for line in f if line.strip()]
        else:
            # Read from stdin
            texts = [line.strip() for line in sys.stdin if line.strip()]

        if not texts:
            logger.error("No input texts provided")
            sys.exit(1)

        # Apply preprocessing if requested
        if args.preprocess:
            texts = [preprocess_text(text) for text in texts]

        # Apply chunking if requested
        if args.chunk_size > 0:
            chunked_texts = []
            for text in texts:
                chunks = chunk_text(
                    text=text,
                    chunk_size=args.chunk_size,
                    chunk_overlap=args.chunk_overlap,
                )
                chunked_texts.extend(chunks)
            texts = chunked_texts

        logger.info(f"Encoding {len(texts)} texts")

        # Initialize model
        if args.model_id == "mock":
            model = MockEmbedding(
                embedding_size=args.embedding_size,
                model_id="mock-embedding",
            )
        else:
            embeddings = TextEmbedding(
                model_id=args.model_id,
                revision=args.revision,
                cache_dir=args.cache_dir,
                use_fp16=not args.no_fp16,
            )
            model = embeddings.model

        # Generate embeddings
        start_time = time.time()

        if args.batch_size > 1:
            # Process in batches
            batch_embeddings = []
            for i in range(0, len(texts), args.batch_size):
                batch = texts[i : i + args.batch_size]
                batch_result = model.encode(batch)
                batch_embeddings.extend(batch_result)
            embeddings_array = batch_embeddings
        else:
            # Process individually
            embeddings_array = model.encode(texts)

        end_time = time.time()

        logger.info(
            f"Generated {len(embeddings_array)} embeddings in {end_time - start_time:.2f} seconds"
        )

        # Output results
        if args.output_file:
            output_path = Path(args.output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            if output_path.suffix == ".json":
                # Output as JSON
                output_data = {
                    "texts": texts,
                    "embeddings": [embedding.tolist() for embedding in embeddings_array],
                    "model_id": model.model_id,
                    "embedding_size": embeddings_array[0].shape[0],
                }

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(output_data, f, indent=2)
            else:
                # Output as text (one embedding per line)
                with open(output_path, "w", encoding="utf-8") as f:
                    for embedding in embeddings_array:
                        embedding_str = ",".join(f"{value:.6f}" for value in embedding)
                        f.write(f"{embedding_str}\n")

            logger.info(f"Saved embeddings to {output_path}")
        else:
            # Output to stdout
            for i, embedding in enumerate(embeddings_array):
                embedding_str = ",".join(f"{value:.6f}" for value in embedding)
                print(f"Text {i}: {embedding_str[:100]}...")

    except Exception as e:
        logger.error(f"Error generating embeddings: {str(e)}")
        sys.exit(1)


def main(args: Optional[List[str]] = None) -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="LLaMA MLX Embeddings Command Line Interface",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--version", action="version", version=f"llamamlx-embeddings v{__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Convert command
    convert_parser = subparsers.add_parser(
        "convert",
        help="Convert a Hugging Face model to MLX format",
    )
    convert_parser.add_argument(
        "model_id",
        help="Hugging Face model ID or path",
    )
    convert_parser.add_argument(
        "--output-dir",
        help="Output directory for the converted model",
    )
    convert_parser.add_argument(
        "--revision",
        help="Model revision to use",
    )
    convert_parser.add_argument(
        "--dtype",
        choices=["float16", "float32"],
        default="float16",
        help="Data type for model weights",
    )
    convert_parser.add_argument(
        "--quantize",
        action="store_true",
        help="Quantize model weights",
    )
    convert_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files",
    )
    convert_parser.set_defaults(func=convert_command)

    # Serve command
    serve_parser = subparsers.add_parser(
        "serve",
        help="Start the API server",
    )
    serve_parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind the server to",
    )
    serve_parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the server to",
    )
    serve_parser.add_argument(
        "--model",
        help="Model ID or path to use",
    )
    serve_parser.add_argument(
        "--device",
        help="Device to use (cpu, gpu, mps)",
    )
    serve_parser.add_argument(
        "--max-length",
        type=int,
        help="Maximum sequence length",
    )
    serve_parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level",
    )
    serve_parser.set_defaults(func=serve_command)

    # List models command
    list_models_parser = subparsers.add_parser(
        "list-models",
        help="List supported models",
    )
    list_models_parser.set_defaults(func=list_models_command)

    # Download command
    download_parser = subparsers.add_parser(
        "download",
        help="Download a model",
    )
    download_parser.add_argument(
        "model_id",
        help="Model ID or path to download",
    )
    download_parser.add_argument(
        "--revision",
        help="Model revision to use",
    )
    download_parser.add_argument(
        "--cache-dir",
        help="Cache directory for models",
    )
    download_parser.add_argument(
        "--no-fp16",
        action="store_true",
        help="Disable FP16 precision",
    )
    download_parser.set_defaults(func=download_command)

    # Benchmark command
    benchmark_parser = subparsers.add_parser(
        "benchmark",
        help="Benchmark a model",
    )
    benchmark_parser.add_argument(
        "model_id",
        help="Model ID or path to benchmark (use 'mock' for mock model)",
    )
    benchmark_parser.add_argument(
        "--batch-sizes",
        default="1,8,32,64",
        help="Comma-separated list of batch sizes to test",
    )
    benchmark_parser.add_argument(
        "--n-samples",
        type=int,
        default=100,
        help="Number of samples to generate",
    )
    benchmark_parser.add_argument(
        "--warmup",
        type=int,
        default=10,
        help="Number of warmup iterations",
    )
    benchmark_parser.add_argument(
        "--output",
        help="Path to save benchmark results",
    )
    benchmark_parser.add_argument(
        "--revision",
        help="Model revision to use",
    )
    benchmark_parser.add_argument(
        "--cache-dir",
        help="Cache directory for models",
    )
    benchmark_parser.add_argument(
        "--no-fp16",
        action="store_true",
        help="Disable FP16 precision",
    )
    benchmark_parser.add_argument(
        "--embedding-size",
        type=int,
        default=768,
        help="Embedding size for mock model",
    )
    benchmark_parser.set_defaults(func=benchmark_command)

    # Embed command
    embed_parser = subparsers.add_parser(
        "embed",
        help="Generate embeddings for texts",
    )
    embed_parser.add_argument(
        "--model-id",
        default="mock",
        help="Model ID or path to use (default: mock)",
    )
    embed_parser.add_argument(
        "--input-file",
        help="Input file containing texts (JSON or text, one per line)",
    )
    embed_parser.add_argument(
        "--output-file",
        help="Output file for embeddings (JSON or text)",
    )
    embed_parser.add_argument(
        "--batch-size",
        type=int,
        default=1,
        help="Batch size for processing",
    )
    embed_parser.add_argument(
        "--preprocess",
        action="store_true",
        help="Apply text preprocessing",
    )
    embed_parser.add_argument(
        "--chunk-size",
        type=int,
        default=0,
        help="Maximum chunk size in tokens (0 to disable chunking)",
    )
    embed_parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=64,
        help="Overlap between chunks in tokens",
    )
    embed_parser.add_argument(
        "--revision",
        help="Model revision to use",
    )
    embed_parser.add_argument(
        "--cache-dir",
        help="Cache directory for models",
    )
    embed_parser.add_argument(
        "--no-fp16",
        action="store_true",
        help="Disable FP16 precision",
    )
    embed_parser.add_argument(
        "--embedding-size",
        type=int,
        default=768,
        help="Embedding size for mock model",
    )
    embed_parser.set_defaults(func=embed_command)

    # Parse arguments
    parsed_args = parser.parse_args(args)

    if parsed_args.command is None:
        parser.print_help()
        sys.exit(0)

    # Execute command
    if hasattr(parsed_args, "func"):
        parsed_args.func(parsed_args)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
