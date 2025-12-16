"""FastAPI main application module.

This module initializes the FastAPI application and mounts mock service routers.
It serves as the entry point for the LLM Mock API Server.
"""

from typing import Dict

from fastapi import FastAPI

from app.mocks import openai_router

app = FastAPI(
    title="LLM Mock API Server",
    description="Mock API server for testing LLM applications locally",
    version="1.0.0",
)


@app.get("/health")
def health_check() -> Dict[str, str]:
    """Health check endpoint to verify the server is running.

    Returns:
        Dict[str, str]: Status dictionary with 'status' key set to 'ok'.
    """
    return {"status": "ok"}


# Mount mock service routers
app.include_router(openai_router, tags=["OpenAI Mock"])


# To add more mock services in the future:
# 1. Create a new module in app/mocks/ (e.g., pinecone_mock.py)
# 2. Export the router in app/mocks/__init__.py
# 3. Import and mount it here:
#    from app.mocks import pinecone_router
#    app.include_router(pinecone_router, tags=["Pinecone Mock"])
