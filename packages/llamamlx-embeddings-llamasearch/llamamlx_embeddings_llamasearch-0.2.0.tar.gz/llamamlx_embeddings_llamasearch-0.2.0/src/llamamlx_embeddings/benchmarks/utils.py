"""
Benchmark utilities for llamamlx-embeddings.
"""

import json
import logging
import random
import string
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import numpy as np

# Configure logging
logger = logging.getLogger(__name__)

# Define sample words for generating more realistic random text
SAMPLE_WORDS = [
    "embedding",
    "vector",
    "semantic",
    "similarity",
    "search",
    "transformer",
    "neural",
    "network",
    "language",
    "model",
    "machine",
    "learning",
    "artificial",
    "intelligence",
    "data",
    "text",
    "document",
    "query",
    "retrieval",
    "classification",
    "clustering",
    "dimension",
    "reduction",
    "tokenization",
    "bert",
    "mlx",
    "apple",
    "silicon",
    "optimization",
    "performance",
]


def generate_random_text(min_length: int = 100, max_length: int = 500) -> str:
    """
    Generate random text with words for testing.

    Args:
        min_length: Minimum length of generated text
        max_length: Maximum length of generated text

    Returns:
        Randomly generated text
    """
    # Determine target length
    target_length = random.randint(min_length, max_length)

    # Generate random text
    words = []
    current_length = 0

    while current_length < target_length:
        # 70% chance to use a sample word, 30% chance for random string
        if random.random() < 0.7:
            word = random.choice(SAMPLE_WORDS)
        else:
            # Generate random word with length 3-10
            word_length = random.randint(3, 10)
            word = "".join(random.choice(string.ascii_lowercase) for _ in range(word_length))

        words.append(word)
        current_length += len(word) + 1  # +1 for space

    # Join words with spaces and occasional punctuation
    result = ""
    for i, word in enumerate(words):
        # Add word
        result += word

        # Add punctuation occasionally
        if random.random() < 0.1:
            result += random.choice([",", ".", ";", ":", "?", "!"])

        # Add space unless it's the last word
        if i < len(words) - 1:
            result += " "

        # Add period and start new sentence occasionally
        if random.random() < 0.05:
            result += ". "
            # Capitalize next word if not the last one
            if i < len(words) - 1:
                words[i + 1] = words[i + 1].capitalize()

    return result


def generate_random_texts(
    count: int = 10, min_length: int = 100, max_length: int = 500
) -> List[str]:
    """
    Generate multiple random texts for testing.

    Args:
        count: Number of texts to generate
        min_length: Minimum length of each text
        max_length: Maximum length of each text

    Returns:
        List of randomly generated texts
    """
    return [generate_random_text(min_length, max_length) for _ in range(count)]


def time_function(
    func: Callable, *args, n_runs: int = 5, warmup: int = 1, **kwargs
) -> Dict[str, Any]:
    """
    Measure execution time of a function.

    Args:
        func: Function to time
        *args: Arguments to pass to the function
        n_runs: Number of runs for measurement
        warmup: Number of warmup runs
        **kwargs: Keyword arguments to pass to the function

    Returns:
        Dictionary with timing statistics
    """
    # Run warmup iterations
    for _ in range(warmup):
        func(*args, **kwargs)

    # Measure execution time
    times = []
    for _ in range(n_runs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        times.append(end_time - start_time)

    # Calculate statistics
    times_array = np.array(times)
    stats = {
        "mean": float(np.mean(times_array)),
        "median": float(np.median(times_array)),
        "min": float(np.min(times_array)),
        "max": float(np.max(times_array)),
        "std": float(np.std(times_array)),
        "n_runs": n_runs,
        "warmup": warmup,
    }

    return stats


def compare_embeddings(
    model_a_embeds: List[np.ndarray], model_b_embeds: List[np.ndarray]
) -> Dict[str, float]:
    """
    Compare embeddings from two different models.

    Args:
        model_a_embeds: List of embeddings from first model
        model_b_embeds: List of embeddings from second model

    Returns:
        Dictionary with comparison metrics
    """
    if len(model_a_embeds) != len(model_b_embeds):
        raise ValueError("Embedding lists must have the same length")

    # Calculate cosine similarities between corresponding embeddings
    similarities = []
    for i in range(len(model_a_embeds)):
        # Normalize embeddings
        a_norm = np.linalg.norm(model_a_embeds[i])
        b_norm = np.linalg.norm(model_b_embeds[i])

        if a_norm > 0 and b_norm > 0:
            a_normalized = model_a_embeds[i] / a_norm
            b_normalized = model_b_embeds[i] / b_norm
            similarity = np.dot(a_normalized, b_normalized)
            similarities.append(similarity)

    # Calculate metrics
    similarities = np.array(similarities)
    metrics = {
        "mean_similarity": float(np.mean(similarities)),
        "min_similarity": float(np.min(similarities)),
        "max_similarity": float(np.max(similarities)),
        "std_similarity": float(np.std(similarities)),
    }

    return metrics


def save_benchmark_results(
    results: Dict[str, Any], filename: str, directory: Optional[str] = None
) -> str:
    """
    Save benchmark results to a JSON file.

    Args:
        results: Benchmark results dictionary
        filename: Name of the file (without directory)
        directory: Directory to save the file (default: current directory)

    Returns:
        Path to the saved file
    """

    # Convert numpy values to Python types for JSON serialization
    def convert_to_serializable(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, (list, tuple)):
            return [convert_to_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: convert_to_serializable(v) for k, v in obj.items()}
        else:
            return obj

    # Convert results to serializable format
    serializable_results = convert_to_serializable(results)

    # Ensure filename has .json extension
    if not filename.endswith(".json"):
        filename += ".json"

    # Create output path
    if directory:
        output_path = Path(directory) / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path(filename)

    # Save results
    with open(output_path, "w") as f:
        json.dump(serializable_results, f, indent=2)

    logger.info(f"Saved benchmark results to {output_path}")
    return str(output_path)


def load_benchmark_results(filepath: str) -> Dict[str, Any]:
    """
    Load benchmark results from a JSON file.

    Args:
        filepath: Path to the JSON file

    Returns:
        Dictionary with benchmark results
    """
    with open(filepath, "r") as f:
        results = json.load(f)

    logger.info(f"Loaded benchmark results from {filepath}")
    return results
