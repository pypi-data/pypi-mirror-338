# Contributing to llamamlx-embeddings

Thank you for your interest in contributing to `llamamlx-embeddings`! This document provides guidelines and instructions for contributing to this project.

## Getting Started

### Requirements

- Python 3.8 or newer
- Git
- For MLX support:
  - macOS running on Apple Silicon (M1/M2/M3)
  - macOS 12.0 (Monterey) or newer

### Development Environment Setup

1. **Fork the repository**

   Start by forking the [repository](https://github.com/yourusername/llamamlx-embeddings) on GitHub.

2. **Clone your fork locally**

   ```bash
   git clone https://github.com/YOUR_USERNAME/llamamlx-embeddings.git
   cd llamamlx-embeddings
   ```

3. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

4. **Install in development mode**

   ```bash
   pip install -e ".[dev]"
   ```

5. **Set up pre-commit hooks**

   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Development Workflow

### Branching Strategy

- `main` branch is the stable, production-ready code
- Feature branches should be created for new features and fixes
- Use descriptive branch names, e.g., `feature/add-new-model-type` or `fix/correct-embedding-normalization`

```bash
git checkout -b feature/your-feature-name
```

### Code Style

This project follows the [Black](https://black.readthedocs.io/) code style. We use isort for organizing imports and flake8 for linting.

- Format your code with Black:

  ```bash
  black .
  ```

- Sort imports with isort:

  ```bash
  isort .
  ```

- Check code quality with flake8:

  ```bash
  flake8 llamamlx_embeddings tests
  ```

- Check type hints with mypy:

  ```bash
  mypy llamamlx_embeddings
  ```

### Running Tests

We use pytest for testing:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=llamamlx_embeddings

# Run a specific test
pytest tests/test_specific.py
```

### Adding New Features

When adding new features:

1. Add appropriate tests in the `tests/` directory
2. Update documentation in the `docs/` directory
3. Add example usage in the `examples/` directory if applicable
4. Update the README if needed

### Adding a New Model Type

1. Update supported models in `llamamlx_embeddings/core/models.py`
2. Add model class in the appropriate module
3. Add tests for the new model type
4. Add documentation

### Creating Pull Requests

1. Ensure your code passes all tests
2. Update documentation as needed
3. Commit your changes with clear, descriptive messages
4. Push your branch to your fork
5. Create a pull request to the `main` branch of the original repository
6. Describe your changes in detail in the PR description

## Documentation

### Docstrings

We follow [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings). Every public function, class, and method should have a docstring.

Example:

```python
def embed_query(self, query: str, **kwargs) -> np.ndarray:
    """
    Generate an embedding for a query text.
    
    This method is optimized for query embeddings, which might be processed
    differently than document embeddings in some models.
    
    Args:
        query: The query text to embed
        **kwargs: Additional arguments to pass to the embedding function
        
    Returns:
        A numpy array containing the query embedding
        
    Raises:
        ValueError: If the query is empty or not a string
    """
```

### Documentation Files

- Update the Markdown documentation in the `docs/` directory
- For significant changes, add examples to the appropriate docs or examples

## Release Process

1. Update version in `llamamlx_embeddings/version.py`
2. Update `CHANGELOG.md`
3. Create a pull request for the release
4. Once merged, create a new GitHub release with the version number
5. The CI/CD workflow will automatically publish to PyPI

## Additional Notes

### Working with MLX and ONNX

When working with model implementations, consider both MLX and ONNX environments:

- Test MLX implementations on Apple Silicon
- Test ONNX fallbacks on non-Apple hardware

### Performance Considerations

- Include benchmarks for significant algorithm changes
- Consider memory usage, especially for large models and batches

## Community

- Be respectful and inclusive of all contributors
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)
- Open issues for discussion before making major changes

Thank you for contributing to `llamamlx-embeddings`! 