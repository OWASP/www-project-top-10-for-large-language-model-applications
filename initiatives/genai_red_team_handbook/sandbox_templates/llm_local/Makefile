.PHONY: help install sync lock build up down test test-client ollama-pull ollama-serve gradio format mypy clean

# Default target
help:
	@echo "LLM Mock API Template - Available Commands:"
	@echo ""
	@echo "  make build         - Build the container image"
	@echo "  make up            - Run the built container"
	@echo "  make down          - Stop and remove the container"
	@echo "  make test          - Test the health endpoint"
	@echo "  make test-client   - Run automated prompt tests from config/prompts.toml"
	@echo "  make clean         - Clean up containers and images"
	@echo ""
	@echo "  make install       - Install uv package manager"
	@echo "  make sync          - Sync/install project dependencies"
	@echo "  make lock          - Update dependency lock file"
	@echo ""
	@echo "  make gradio        - Full setup: sync, lock, clean, build, start server, and launch UI"
	@echo "                       (requires Ollama to be running first)"
	@echo ""
	@echo "  make format        - Run black and isort formatters"
	@echo "  make mypy          - Run mypy static type checker"
	@echo ""
	@echo "  make ollama-pull   - Pull llama3 model for Ollama"
	@echo "  make ollama-serve  - Start Ollama server"
	@echo ""
	@echo "Environment:"
	@echo "  - Ensure Ollama is running locally (port 11434)"
	@echo "  - Mock API key: sk-mock-key"
	@echo "  - API endpoint: http://localhost:8000"
	@echo ""

install:
	pip install uv

sync:
	uv sync

lock:
	uv lock

build:
	podman build -f Containerfile -t openai-mock-api .

up:
	podman run -d --name app_container -p 8000:8000 -v ./data:/app/data openai-mock-api

down:
	podman rm -f app_container

clean:
	@echo "🧹 Cleaning up containers and images..."
	-podman rm -f app_container 2>/dev/null || true
	-podman rmi openai-mock-api 2>/dev/null || true
	@echo "✅ Cleanup complete!"

ollama-pull:
	ollama pull llama3

ollama-serve:
	@echo "🔍 Checking if Ollama is running..."
	@if lsof -Pi :11434 -sTCP:LISTEN -t >/dev/null 2>&1; then \
		echo "✅ Ollama is already running on port 11434"; \
	else \
		echo "🚀 Starting Ollama server..."; \
		ollama serve; \
	fi

format:
	@echo "Running black formatter..."
	uv run black app/ client/
	@echo "Running isort import sorter..."
	uv run isort app/ client/
	@echo "✅ Formatting complete!"

mypy:
	@echo "Running mypy type checker..."
	uv run mypy app/ client/
	@echo "✅ Type checking complete!"

test: sync lock clean ollama-pull ollama-serve build up
	@echo "⏳ Waiting for server to start..."
	@sleep 3
	@curl -s http://localhost:8000/health | grep ok && echo " ✅ Server is healthy!"

test-client: sync lock clean ollama-pull ollama-serve build up test
	podman exec app_container uv run python client/main.py

gradio: sync lock clean ollama-pull ollama-serve build up test test-client
	@echo "🧹 Stopping any existing Gradio instance..."
	@-lsof -ti:7860 | xargs kill -9 2>/dev/null || true
	@echo "🚀 Starting Gradio interface..."
	@uv run python client/gradio_app.py & sleep 3 && open http://localhost:7860
