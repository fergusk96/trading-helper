PYTHON = python
PIP = pip
PYTEST = pytest

# Define targets
.PHONY: install test

# Install dependencies
install:
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt


# Run tests
test:
	$(PYTEST)
