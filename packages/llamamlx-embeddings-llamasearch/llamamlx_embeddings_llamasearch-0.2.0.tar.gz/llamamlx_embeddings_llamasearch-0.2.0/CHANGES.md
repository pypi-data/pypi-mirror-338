# Repository Cleanup and Fixes

This document summarizes the changes made to clean up and fix issues in the `llamamlx-embeddings` repository.

## Changes Made in v0.2.0

### 1. File Organization
- Moved duplicate and loose files from the root directory to a backup folder
- Removed unused and draft files that were causing confusion
- Consolidated test files into the proper test directory
- Created a dedicated reference folder for documentation and example files
- Moved simple_test.py to the examples directory

### 2. Import Issues
- Fixed unused imports throughout the codebase using autoflake and isort
- Fixed specific import issues in `embeddings.py`
- Resolved named imports in `__init__.py` by using aliases (`register_custom_model as add_custom_model`)
- Added missing `mlx.nn` import in sparse-module.py
- Fixed undefined `__version__` variable in setup-py.py

### 3. Dependency Management
- Updated Pinecone integration to handle the renamed package (from `pinecone-client` to `pinecone`)
- Added proper extra dependencies in setup.py (onnx, pinecone, qdrant, all)
- Improved error messages for missing dependencies
- Created a comprehensive requirements.txt file with optional dependencies

### 4. CI/CD Improvements
- Updated the GitHub Actions workflow (`tests.yml`) to properly handle platform-specific testing
- Modified macOS tests to work on GitHub Actions runners without Apple Silicon
- Created a proper publish workflow for PyPI with secure credentials handling
- Added a run_tests.py script for easy test execution with coverage reporting

### 5. Build System
- Added and updated Makefile with useful development commands
- Fixed version handling in `setup.py` to properly use the version defined in `version.py`
- Created a modern `pyproject.toml` with build-system and tool configurations
- Added MANIFEST.in to include necessary files in the distribution
- Added a comprehensive requirements.txt file

### 6. Documentation
- Updated README.md with version information and recent changes
- Created CHANGES.md to track all changes and improvements
- Added inline documentation for key functions and classes
- Created proper example scripts with documentation
- Added a README.md file for the examples directory

### 7. Testing
- Fixed test structure with proper __init__.py and conftest.py files
- Ensured all tests pass with the mock embeddings
- Created example scripts that demonstrate package functionality
- Verified package installation works correctly

## Files Fixed
- `llamamlx_embeddings/__init__.py`: Fixed imports and dependency handling
- `llamamlx_embeddings/core/embeddings.py`: Fixed unused imports
- `llamamlx_embeddings/integrations/pinecone.py`: Updated for renamed package
- `.github/workflows/tests.yml`: Updated for platform compatibility
- `.github/workflows/publish.yml`: Created for PyPI publishing
- `setup.py`: Fixed version handling and added proper extras
- `pyproject.toml`: Modernized with proper tool configurations
- `backup/sparse-module.py`: Fixed missing import
- `backup/setup-py.py`: Fixed undefined variable
- Multiple files: Code formatting and import clean-up

## Files Added
- `run_tests.py`: Script for running tests with coverage
- `examples/basic_embedding.py`: Example for basic embedding functionality
- `examples/sparse_embedding.py`: Example for sparse embedding functionality
- `examples/README.md`: Documentation for example scripts
- `tests/conftest.py`: Pytest configuration
- `tests/__init__.py`: Package marker for tests
- `tests/benchmarks/__init__.py`: Package marker for benchmark tests

## Files Removed/Moved
- `api-main.py`, `api-init.py`: Moved to backup
- `cli-module.py`: Moved to backup
- `embeddings-module.py`: Moved to backup  
- `models-module.py` variants: Moved to backup
- `onnx-module.py`: Moved to backup
- `quantization-module.py`: Moved to backup
- `sparse-module.py`: Moved to backup
- `pinecone-integration.py`: Moved to backup
- `setup-py.py`: Moved to backup
- `simple_test.py`: Moved to examples
- Various test files and init files: Moved to backup
- Reference text files: Moved to backup/reference

These changes have resulted in a more organized, maintainable codebase with fewer errors and better test reliability. The package is now ready for distribution via PyPI with proper versioning and dependency management. 