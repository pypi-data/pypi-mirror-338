"""
Visualization utilities for benchmark results.
"""

import json
import logging
from pathlib import Path
from typing import Dict, Optional, Union

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .benchmark import BenchmarkResult

# Configure logging
logger = logging.getLogger(__name__)


def load_benchmark_results(file_path: Union[str, Path]) -> Dict[int, BenchmarkResult]:
    """
    Load benchmark results from a JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        Dictionary mapping batch size to benchmark result
    """
    file_path = Path(file_path)

    with open(file_path, "r") as f:
        data = json.load(f)

    results = {}
    for batch_size_str, result_dict in data.items():
        batch_size = int(batch_size_str)

        # Create a BenchmarkResult with dummy batch_times
        result = BenchmarkResult(
            model_name=result_dict["model_name"],
            device=result_dict["device"],
            batch_size=result_dict["batch_size"],
            sequence_length=result_dict["sequence_length"],
            throughput=result_dict["throughput"],
            latency_mean=result_dict["latency_mean"],
            latency_p50=result_dict["latency_p50"],
            latency_p90=result_dict["latency_p90"],
            latency_p99=result_dict["latency_p99"],
            memory_usage=result_dict["memory_usage"],
            batch_times=[],  # Dummy value
        )

        results[batch_size] = result

    return results


def plot_throughput(
    results: Dict[str, Dict[int, BenchmarkResult]],
    output_file: Optional[str] = None,
    figsize: tuple = (10, 6),
    title: str = "Throughput Comparison (Higher is Better)",
) -> None:
    """
    Plot throughput comparison between models.

    Args:
        results: Dictionary mapping model name to benchmark results
        output_file: Path to save the plot
        figsize: Figure size (width, height) in inches
        title: Plot title
    """
    plt.figure(figsize=figsize)

    # Prepare data for plotting
    records = []
    for model_name, model_results in results.items():
        for batch_size, result in model_results.items():
            records.append(
                {
                    "Model": model_name,
                    "Batch Size": batch_size,
                    "Throughput (tokens/s)": result.throughput,
                }
            )

    df = pd.DataFrame(records)

    # Plot
    sns.set_style("whitegrid")
    ax = sns.barplot(x="Batch Size", y="Throughput (tokens/s)", hue="Model", data=df)
    plt.title(title)
    plt.xlabel("Batch Size")
    plt.ylabel("Throughput (tokens/s)")
    plt.legend(title="Model")
    plt.tight_layout()

    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path)
        logger.info(f"Saved throughput plot to {output_path}")

    plt.close()


def plot_latency(
    results: Dict[str, Dict[int, BenchmarkResult]],
    output_file: Optional[str] = None,
    figsize: tuple = (10, 6),
    title: str = "Latency Comparison (Lower is Better)",
    metric: str = "latency_mean",
) -> None:
    """
    Plot latency comparison between models.

    Args:
        results: Dictionary mapping model name to benchmark results
        output_file: Path to save the plot
        figsize: Figure size (width, height) in inches
        title: Plot title
        metric: Latency metric to plot (latency_mean, latency_p50, latency_p90, latency_p99)
    """
    plt.figure(figsize=figsize)

    metric_name = {
        "latency_mean": "Mean Latency (ms)",
        "latency_p50": "Median Latency (ms)",
        "latency_p90": "90th Percentile Latency (ms)",
        "latency_p99": "99th Percentile Latency (ms)",
    }.get(metric, "Latency (ms)")

    # Prepare data for plotting
    records = []
    for model_name, model_results in results.items():
        for batch_size, result in model_results.items():
            records.append(
                {
                    "Model": model_name,
                    "Batch Size": batch_size,
                    metric_name: getattr(result, metric),
                }
            )

    df = pd.DataFrame(records)

    # Plot
    sns.set_style("whitegrid")
    ax = sns.lineplot(x="Batch Size", y=metric_name, hue="Model", marker="o", data=df)
    plt.title(title)
    plt.xlabel("Batch Size")
    plt.ylabel(metric_name)
    plt.legend(title="Model")
    plt.tight_layout()

    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path)
        logger.info(f"Saved latency plot to {output_path}")

    plt.close()


def plot_memory_usage(
    results: Dict[str, Dict[int, BenchmarkResult]],
    output_file: Optional[str] = None,
    figsize: tuple = (10, 6),
    title: str = "Memory Usage Comparison",
) -> None:
    """
    Plot memory usage comparison between models.

    Args:
        results: Dictionary mapping model name to benchmark results
        output_file: Path to save the plot
        figsize: Figure size (width, height) in inches
        title: Plot title
    """
    plt.figure(figsize=figsize)

    # Prepare data for plotting
    records = []
    for model_name, model_results in results.items():
        for batch_size, result in model_results.items():
            records.append(
                {
                    "Model": model_name,
                    "Batch Size": batch_size,
                    "Memory Usage (MB)": result.memory_usage,
                }
            )

    df = pd.DataFrame(records)

    # Plot
    sns.set_style("whitegrid")
    ax = sns.lineplot(x="Batch Size", y="Memory Usage (MB)", hue="Model", marker="o", data=df)
    plt.title(title)
    plt.xlabel("Batch Size")
    plt.ylabel("Memory Usage (MB)")
    plt.legend(title="Model")
    plt.tight_layout()

    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path)
        logger.info(f"Saved memory usage plot to {output_path}")

    plt.close()


def create_comparison_dashboard(
    results: Dict[str, Dict[int, BenchmarkResult]],
    output_dir: Union[str, Path],
    prefix: str = "benchmark",
) -> None:
    """
    Create a comparison dashboard with multiple plots.

    Args:
        results: Dictionary mapping model name to benchmark results
        output_dir: Directory to save the plots
        prefix: Prefix for output files
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Plot throughput
    plot_throughput(
        results,
        output_file=output_dir / f"{prefix}_throughput.png",
        title="Throughput Comparison (Higher is Better)",
    )

    # Plot latency metrics
    plot_latency(
        results,
        output_file=output_dir / f"{prefix}_latency_mean.png",
        title="Mean Latency Comparison (Lower is Better)",
        metric="latency_mean",
    )

    plot_latency(
        results,
        output_file=output_dir / f"{prefix}_latency_p90.png",
        title="90th Percentile Latency Comparison (Lower is Better)",
        metric="latency_p90",
    )

    # Plot memory usage
    plot_memory_usage(
        results,
        output_file=output_dir / f"{prefix}_memory_usage.png",
        title="Memory Usage Comparison",
    )

    # Create comparison table
    records = []
    for model_name, model_results in results.items():
        for batch_size, result in model_results.items():
            records.append(
                {
                    "Model": model_name,
                    "Batch Size": batch_size,
                    "Throughput (tokens/s)": result.throughput,
                    "Mean Latency (ms)": result.latency_mean,
                    "Median Latency (ms)": result.latency_p50,
                    "90th Percentile Latency (ms)": result.latency_p90,
                    "99th Percentile Latency (ms)": result.latency_p99,
                    "Memory Usage (MB)": result.memory_usage,
                }
            )

    df = pd.DataFrame(records)
    df.to_csv(output_dir / f"{prefix}_comparison.csv", index=False)

    # Create HTML report
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Benchmark Comparison</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            .container { display: flex; flex-wrap: wrap; }
            .chart { margin: 10px; box-shadow: 0 0 5px #ccc; padding: 10px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            tr:nth-child(even) { background-color: #f9f9f9; }
        </style>
    </head>
    <body>
        <h1>Benchmark Comparison</h1>
        
        <div class="container">
            <div class="chart">
                <h2>Throughput Comparison</h2>
                <img src="{prefix}_throughput.png" alt="Throughput Comparison">
            </div>
            
            <div class="chart">
                <h2>Mean Latency Comparison</h2>
                <img src="{prefix}_latency_mean.png" alt="Mean Latency Comparison">
            </div>
            
            <div class="chart">
                <h2>90th Percentile Latency Comparison</h2>
                <img src="{prefix}_latency_p90.png" alt="90th Percentile Latency Comparison">
            </div>
            
            <div class="chart">
                <h2>Memory Usage Comparison</h2>
                <img src="{prefix}_memory_usage.png" alt="Memory Usage Comparison">
            </div>
        </div>
        
        <h2>Detailed Comparison</h2>
        <p>See the <a href="{prefix}_comparison.csv">CSV file</a> for detailed comparison data.</p>
    </body>
    </html>
    """.format(
        prefix=prefix
    )

    with open(output_dir / f"{prefix}_report.html", "w") as f:
        f.write(html)

    logger.info(f"Created comparison dashboard in {output_dir}")
