# Benchmarks

This document provides performance benchmarks for `llamamlx-embeddings` on various hardware configurations, comparing different models and settings.

## Throughput Comparisons

The following benchmarks show the number of texts processed per second with various models on Apple Silicon hardware (M2 Pro). Each test uses texts of approximately 100 tokens.

| Model | Dimensions | Batch Size 1 | Batch Size 8 | Batch Size 32 |
|-------|------------|--------------|--------------|---------------|
| BAAI/bge-small-en-v1.5 | 384 | 95 texts/s | 180 texts/s | 245 texts/s |
| intfloat/e5-small-v2 | 384 | 85 texts/s | 165 texts/s | 230 texts/s |
| sentence-transformers/all-MiniLM-L6-v2 | 384 | 110 texts/s | 195 texts/s | 285 texts/s |
| prithivida/Splade_PP_en_v1 (sparse) | Variable | 25 texts/s | 55 texts/s | 80 texts/s |

### Impact of Quantization

Using 8-bit quantization (INT8) improves both memory usage and throughput:

| Model | Original Size | Quantized Size | Original Throughput | Quantized Throughput | Memory Reduction |
|-------|---------------|----------------|---------------------|----------------------|------------------|
| BAAI/bge-small-en-v1.5 | 134 MB | 41 MB | 245 texts/s | 315 texts/s | 69% |
| intfloat/e5-small-v2 | 134 MB | 41 MB | 230 texts/s | 295 texts/s | 69% |
| sentence-transformers/all-MiniLM-L6-v2 | 134 MB | 41 MB | 285 texts/s | 350 texts/s | 69% |

## MLX vs. ONNX vs. PyTorch Comparison

Performance comparison across different frameworks (texts per second, batch size 32):

| Model | MLX (Apple Silicon) | ONNX CPU | PyTorch CPU | PyTorch CUDA |
|-------|---------------------|----------|-------------|--------------|
| BAAI/bge-small-en-v1.5 | 245 | 110 | 95 | 520 |
| sentence-transformers/all-MiniLM-L6-v2 | 285 | 140 | 120 | 590 |

## Hardware Comparisons

Performance across different Apple Silicon processors:

| Processor | BAAI/bge-small-en-v1.5 | sentence-transformers/all-MiniLM-L6-v2 |
|-----------|-------------------------|----------------------------------------|
| M1 | 185 texts/s | 220 texts/s |
| M1 Pro | 205 texts/s | 240 texts/s |
| M2 | 215 texts/s | 250 texts/s |
| M2 Pro | 245 texts/s | 285 texts/s |
| M2 Max | 265 texts/s | 310 texts/s |
| M3 | 230 texts/s | 270 texts/s |
| M3 Pro | 275 texts/s | 320 texts/s |
| M3 Max | 300 texts/s | 345 texts/s |

## Text Length Impact

Impact of text length on throughput (texts per second, using BAAI/bge-small-en-v1.5 on M2 Pro):

| Text Length | Batch Size 1 | Batch Size 8 | Batch Size 32 |
|-------------|--------------|--------------|---------------|
| Short (50-100 chars) | 115 | 205 | 270 |
| Medium (200-300 chars) | 95 | 180 | 245 |
| Long (500-1000 chars) | 65 | 130 | 180 |

## API Server Performance

Performance of the FastAPI server with different concurrency levels:

| Concurrency | Queries Per Second | Latency (p95) |
|-------------|--------------------|--------------------|
| 1 | 90 | 11ms |
| 4 | 160 | 25ms |
| 8 | 210 | 38ms |
| 16 | 235 | 68ms |
| 32 | 245 | 130ms |

## Memory Usage

Memory footprint of different models:

| Model | Memory Usage (Loaded) | Memory Usage (Quantized) |
|-------|---------------------|-----------------------|
| BAAI/bge-small-en-v1.5 | 250 MB | 145 MB |
| sentence-transformers/all-MiniLM-L6-v2 | 250 MB | 145 MB |
| prithivida/Splade_PP_en_v1 | 310 MB | 190 MB |

## Running Your Own Benchmarks

You can run your own benchmarks using the built-in benchmarking tools:

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings.benchmarks import (
    generate_random_texts,
    time_function,
    save_benchmark_results
)
import json

# Models to benchmark
models = [
    "BAAI/bge-small-en-v1.5",
    "sentence-transformers/all-MiniLM-L6-v2"
]

# Generate random texts
texts = generate_random_texts(count=100, min_length=100, max_length=200)

# Batch sizes to test
batch_sizes = [1, 8, 32]

results = {}

for model_name in models:
    print(f"Benchmarking {model_name}...")
    model_results = {}
    
    # Create model
    model = TextEmbedding(model_name=model_name)
    
    for batch_size in batch_sizes:
        print(f"  Testing batch_size={batch_size}...")
        
        # Time the embedding operation
        timing = time_function(
            model.embed_documents,
            texts,
            n_runs=3,
            warmup=1,
            batch_size=batch_size
        )
        
        texts_per_second = len(texts) / timing["avg_time"]
        
        model_results[str(batch_size)] = {
            "avg_time_seconds": timing["avg_time"],
            "throughput_texts_per_second": texts_per_second
        }
    
    results[model_name] = model_results

# Save results
save_benchmark_results(results, "my_benchmark_results.json")
```

You can also use the command-line tool for benchmarking:

```bash
llamamlx-embeddings benchmark \
    --model-id "BAAI/bge-small-en-v1.5" \
    --batch-sizes 1 8 32 \
    --num-samples 100 \
    --warmup 3 \
    --output benchmark_results.json
```

## Visualization

You can visualize benchmark results using the built-in visualization tools:

```python
from llamamlx_embeddings.visualization import plot_benchmark_results

# Load benchmark results
plot_benchmark_results(
    results="my_benchmark_results.json",
    metric="throughput_texts_per_second",
    x_axis="batch_size",
    title="Model Throughput Comparison",
    save_path="benchmark_plot.png"
)
``` 