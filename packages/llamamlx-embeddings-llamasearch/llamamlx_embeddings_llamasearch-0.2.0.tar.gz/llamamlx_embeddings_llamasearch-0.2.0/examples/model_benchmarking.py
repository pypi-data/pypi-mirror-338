#!/usr/bin/env python
"""
Example of benchmarking embedding models using llamamlx-embeddings.
"""

import logging
import time
import numpy as np
import os
import json
import random
from typing import List, Dict, Any, Tuple
import matplotlib.pyplot as plt
import sys

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings.core.mock_embeddings import MockEmbedding
from llamamlx_embeddings import configure_logging

# Configure logging
configure_logging(level="INFO")
logger = logging.getLogger(__name__)


# Utility functions for benchmarking
def generate_random_texts(
    n_texts: int, 
    min_length: int = 100, 
    max_length: int = 500, 
    seed: int = 42
) -> List[str]:
    """
    Generate random texts for benchmarking.
    
    Args:
        n_texts: Number of texts to generate
        min_length: Minimum text length (words)
        max_length: Maximum text length (words)
        seed: Random seed for reproducibility
        
    Returns:
        List of random texts
    """
    random.seed(seed)
    
    # Create a word list for random text generation
    base_words = [
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "I", 
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
        "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
        "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
        "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
        "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
        "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
        "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
        "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
    ]
    
    # Generate texts
    texts = []
    for _ in range(n_texts):
        length = random.randint(min_length, max_length)
        text = " ".join(random.choice(base_words) for _ in range(length))
        texts.append(text)
        
    return texts


def plot_benchmark_results(results: Dict[str, Any], output_file: str = "benchmark_plot.png"):
    """
    Simple plot for benchmark results.
    
    Args:
        results: Benchmark results
        output_file: Output file path
    """
    # Extract data for plotting
    batch_sizes = sorted(set(m["batch_size"] for m in results["measurements"]))
    text_lengths = sorted(set(m["text_length"] for m in results["measurements"]))
    
    # Create a figure with subplots for each text length
    fig, axes = plt.subplots(1, len(text_lengths), figsize=(5*len(text_lengths), 5))
    if len(text_lengths) == 1:
        axes = [axes]
    
    for i, text_length in enumerate(text_lengths):
        data = [m for m in results["measurements"] if m["text_length"] == text_length]
        x = [m["batch_size"] for m in data]
        y = [m["throughput_texts_per_second"] for m in data]
        
        axes[i].plot(x, y, 'o-', linewidth=2)
        axes[i].set_title(f"Text Length: {text_length}")
        axes[i].set_xlabel("Batch Size")
        axes[i].set_ylabel("Throughput (texts/s)")
        axes[i].grid(True)
        
    plt.tight_layout()
    plt.savefig(output_file)
    logger.info(f"Plot saved to {output_file}")


def benchmark_embedding_model(
    model, 
    batch_sizes: List[int] = [1, 2, 4, 8, 16],
    text_lengths: List[int] = [128, 512, 1024],
    n_samples: int = 5,
    warmup_iterations: int = 2
) -> Dict[str, Any]:
    """
    Benchmark an embedding model with different batch sizes and text lengths.
    
    Args:
        model: The embedding model to benchmark
        batch_sizes: List of batch sizes to test
        text_lengths: List of text lengths to test
        n_samples: Number of times to run each configuration
        warmup_iterations: Number of warmup iterations before timing
        
    Returns:
        Dictionary with benchmark results
    """
    results = {
        "model_id": getattr(model, "model_id", "unknown"),
        "embedding_size": getattr(model, "embedding_size", 0),
        "batch_sizes": batch_sizes,
        "text_lengths": text_lengths,
        "n_samples": n_samples,
        "warmup_iterations": warmup_iterations,
        "measurements": []
    }
    
    for text_length in text_lengths:
        logger.info(f"Benchmarking with text length: {text_length}")
        
        # Generate random texts for this length
        texts = generate_random_texts(100, min_length=text_length, max_length=text_length)
        
        for batch_size in batch_sizes:
            if batch_size > len(texts):
                continue
                
            logger.info(f"  Batch size: {batch_size}")
            
            # Warmup
            for _ in range(warmup_iterations):
                model.encode(texts[:batch_size])
            
            # Measurements
            batch_times = []
            batch_texts = texts[:batch_size]
            
            for i in range(n_samples):
                start_time = time.time()
                embeddings = model.encode(batch_texts)
                end_time = time.time()
                
                batch_times.append(end_time - start_time)
                
            # Calculate statistics
            avg_time = np.mean(batch_times)
            std_time = np.std(batch_times)
            min_time = np.min(batch_times)
            max_time = np.max(batch_times)
            
            # Calculate throughput (texts/second)
            throughput = batch_size / avg_time
            
            # Add to results
            results["measurements"].append({
                "text_length": text_length,
                "batch_size": batch_size,
                "avg_time_seconds": float(avg_time),
                "std_time_seconds": float(std_time),
                "min_time_seconds": float(min_time),
                "max_time_seconds": float(max_time),
                "throughput_texts_per_second": float(throughput)
            })
            
            logger.info(f"    Average time: {avg_time:.4f}s, Throughput: {throughput:.2f} texts/s")
    
    return results


def save_benchmark_results(results: Dict[str, Any], filename: str = "benchmark_results.json"):
    """
    Save benchmark results to a JSON file.
    
    Args:
        results: Benchmark results
        filename: Output filename
    """
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    
    logger.info(f"Benchmark results saved to {filename}")


def main():
    print("\n" + "="*80)
    print("Model Benchmarking Example using llamamlx-embeddings")
    print("="*80)
    
    # Initialize mock embedding models with different sizes
    models = [
        MockEmbedding(embedding_size=384, model_id="mock-small"),
        MockEmbedding(embedding_size=768, model_id="mock-medium"),
        MockEmbedding(embedding_size=1024, model_id="mock-large")
    ]
    
    # Define benchmark parameters
    batch_sizes = [1, 4, 16]
    text_lengths = [128, 512]
    n_samples = 3
    warmup_iterations = 1
    
    # Run benchmarks for each model
    all_results = []
    
    for model in models:
        print(f"\nBenchmarking model: {model.model_id}")
        print(f"Embedding size: {model.embedding_size}")
        
        results = benchmark_embedding_model(
            model, 
            batch_sizes=batch_sizes,
            text_lengths=text_lengths,
            n_samples=n_samples,
            warmup_iterations=warmup_iterations
        )
        
        all_results.append(results)
        
        # Save individual model results
        save_benchmark_results(results, f"benchmark_{model.model_id}.json")
    
    # Visualize results
    try:
        # Throughput comparison across models
        print("\nGenerating performance comparison charts...")
        
        # Compare throughput across models for text length 512
        models_data = []
        for result in all_results:
            model_data = {
                "model": result["model_id"],
                "batch_sizes": [],
                "throughputs": []
            }
            
            # Extract throughput for text length 512
            for measurement in result["measurements"]:
                if measurement["text_length"] == 512:
                    model_data["batch_sizes"].append(measurement["batch_size"])
                    model_data["throughputs"].append(measurement["throughput_texts_per_second"])
            
            models_data.append(model_data)
        
        # Create simple plot
        plt.figure(figsize=(10, 6))
        
        for model_data in models_data:
            plt.plot(model_data["batch_sizes"], model_data["throughputs"], marker='o', label=model_data["model"])
        
        plt.xlabel('Batch Size')
        plt.ylabel('Throughput (texts/second)')
        plt.title('Embedding Model Throughput Comparison (512 token texts)')
        plt.legend()
        plt.grid(True)
        
        # Save the figure
        plt.savefig('model_throughput_comparison.png')
        print("Throughput comparison saved as 'model_throughput_comparison.png'")
        
        # Also create plots for each individual model
        for result in all_results:
            plot_benchmark_results(result, f"benchmark_plot_{result['model_id']}.png")
        
    except ImportError:
        print("Note: Matplotlib is required for visualization. Install it with 'pip install matplotlib'")


if __name__ == "__main__":
    main() 