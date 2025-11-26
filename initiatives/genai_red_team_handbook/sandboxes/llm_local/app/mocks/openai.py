"""Mock OpenAI API implementation using Ollama as the backend.

This module provides a FastAPI router that mimics the OpenAI chat completions API,
routing requests to a local Ollama instance for testing purposes.
"""

import os
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, Header, HTTPException
from openai import OpenAI
from pydantic import BaseModel

# Configure Ollama as the backend
os.environ["OPENAI_API_KEY"] = "foo"
os.environ["OPENAI_BASE_URL"] = os.getenv(
    "OLLAMA_BASE_URL", "http://host.containers.internal:11434/v1"
)

router = APIRouter()


def verify_api_key(authorization: str = Header(...)) -> str:
    """Mock API key verification for testing purposes.

    In a real implementation, this would validate against a database or secret store.
    For testing purposes, we accept a simple mock key.

    Args:
        authorization: Authorization header value (e.g., "Bearer sk-mock-key").

    Returns:
        str: The extracted API key token.

    Raises:
        HTTPException: If authentication scheme is invalid or API key doesn't match.
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    token = authorization.split(" ")[1]
    if token != "sk-mock-key":
        raise HTTPException(status_code=401, detail="Invalid API key")
    return token


class ChatCompletionRequest(BaseModel):
    """Request model for chat completions endpoint.

    Attributes:
        model: Name of the model to use (e.g., "gpt-oss:20b").
        messages: List of message dictionaries with 'role' and 'content' keys.
        temperature: Sampling temperature between 0 and 2. Defaults to 0.7.
        max_tokens: Maximum number of tokens to generate. Defaults to None.
        top_p: Nucleus sampling parameter. Defaults to None.
        stream: Whether to stream responses. Defaults to False.
    """

    model: str
    messages: List[Dict[str, Any]]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    stream: Optional[bool] = False


# Initialize OpenAI client with Ollama backend
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL", "http://host.containers.internal:11434/v1"),
    api_key="ollama",
)


@router.post("/v1/chat/completions")
def chat_completions(
    request: ChatCompletionRequest, token: str = Depends(verify_api_key)
) -> Any:
    """Mock OpenAI chat completions endpoint using Ollama as the backend.

    This endpoint mimics the OpenAI API but routes requests to a local Ollama instance.
    Useful for testing LLM applications without incurring API costs.

    Args:
        request: Chat completion request with model, messages, and parameters.
        token: Validated API key token from dependency injection.

    Returns:
        Any: OpenAI-compatible chat completion response object.

    Raises:
        HTTPException: If the Ollama backend returns an error (status 500).
    """
    print(f"DEBUG: Received request with messages: {request.messages}")
    try:
        # Type ignore for messages - OpenAI client accepts dict format
        response = client.chat.completions.create(
            model=request.model,
            messages=request.messages,  # type: ignore[arg-type]
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            top_p=request.top_p,
            stream=False if request.stream is None else request.stream,
        )
        return response
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))
