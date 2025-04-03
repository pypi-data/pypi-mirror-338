# Makefile for Prefect MCP Server Repository

.PHONY: install build test deploy clean

# Build the package
build:
	uv run python -m build

# Run tests using pytest (if tests are available)
test:
	pytest

# Deploy package (customize as needed)
deploy:
	uv run twine upload dist/*

# Clean build artifacts
clean:
	rm -rf build dist *.egg-info 