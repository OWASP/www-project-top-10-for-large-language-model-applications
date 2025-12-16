"""Mock API Services package.

This package contains modular mock implementations of various AI/ML services.
Each mock service is implemented as a FastAPI router that can be easily
mounted into the main application.

Available Mocks:
    openai: Mock OpenAI API using Ollama as the backend.
"""

from app.mocks.openai import router as openai_router

__all__ = ["openai_router"]
