.PHONY: help install install-dev clean test test-cov lint format build check deploy docs

help: ## Show this help message
	@echo "Mosaia Python SDK - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package in development mode
	pip install -e .

install-dev: ## Install the package with development dependencies
	pip install -e .[dev]

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

test: ## Run tests
	python -m pytest tests/ -v

test-cov: ## Run tests with coverage
	python -m pytest tests/ --cov=mosaia --cov-report=term-missing --cov-report=html -v

lint: ## Run linting tools
	flake8 mosaia/ tests/
	mypy mosaia/

format: ## Format code
	isort mosaia/ tests/
	black mosaia/ tests/

format-check: ## Check code formatting
	isort --check-only mosaia/ tests/
	black --check mosaia/ tests/

build: ## Build the package
	python -m build

check: ## Check the built package
	twine check dist/*

deploy: ## Deploy to PyPI (requires TWINE_USERNAME and TWINE_PASSWORD)
	twine upload dist/*

deploy-test: ## Deploy to Test PyPI (requires TWINE_USERNAME and TWINE_PASSWORD)
	twine upload --repository testpypi dist/*

docs: ## Build documentation
	cd docs && make html

docs-serve: ## Serve documentation locally
	cd docs/_build/html && python -m http.server 8000

all: clean format lint test build check ## Run all checks and build

ci: format-check lint test build check ## Run CI checks (no code modification)
