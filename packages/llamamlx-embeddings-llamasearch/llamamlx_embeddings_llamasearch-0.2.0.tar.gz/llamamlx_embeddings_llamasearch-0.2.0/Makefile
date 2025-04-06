.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint test test-all

help:
	@echo "Commands:"
	@echo "  clean          Remove all build, test, coverage and Python artifacts"
	@echo "  clean-build    Remove build artifacts"
	@echo "  clean-pyc      Remove Python file artifacts"
	@echo "  clean-test     Remove test and coverage artifacts"
	@echo "  lint           Check style with flake8, black, and isort"
	@echo "  format         Format code with black and isort"
	@echo "  test           Run tests with the default Python"
	@echo "  test-all       Run tests on every Python version with tox"
	@echo "  coverage       Check code coverage quickly with the default Python"
	@echo "  docs           Generate Sphinx HTML documentation"
	@echo "  servedocs      Rebuild Sphinx docs automatically and serve"
	@echo "  dist           Package"
	@echo "  install        Install the package to the active Python's site-packages"
	@echo "  dev-install    Install the package in development mode with all extras"
	@echo "  pre-commit     Install pre-commit hooks"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint:
	flake8 llamamlx_embeddings tests
	black --check llamamlx_embeddings tests
	isort --check-only --profile black llamamlx_embeddings tests
	mypy llamamlx_embeddings

format:
	black llamamlx_embeddings tests
	isort --profile black llamamlx_embeddings tests

test:
	pytest

test-all:
	tox

coverage:
	pytest --cov=llamamlx_embeddings --cov-report=xml --cov-report=term

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

servedocs:
	python -m http.server -d docs/_build/html

dist: clean
	python -m build
	ls -l dist

install: clean
	pip install .

dev-install: clean
	pip install -e ".[dev,all]"

pre-commit:
	pip install pre-commit
	pre-commit install 