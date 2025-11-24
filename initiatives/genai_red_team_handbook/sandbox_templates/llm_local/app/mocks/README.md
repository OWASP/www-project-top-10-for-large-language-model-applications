# Adding New Mock Services

This directory contains modular mock implementations of various AI/ML APIs. Each mock service is implemented as a separate module with its own FastAPI router.

## Structure

```
app/mocks/
├── __init__.py              # Exports all available routers
├── openai.py                # Mock OpenAI API using Ollama
├── README.md                # This file
└── [future_service].py      # Add new mocks here
```

## How to Add a New Mock Service

### 1. Create a New Module

Create a new file in `app/mocks/` for your service, e.g., `pinecone_mock.py`:

```python
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel

router = APIRouter()

def verify_api_key(authorization: str = Header(...)):
    """Mock API key verification for your service."""
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    token = authorization.split(" ")[1]
    # Add your mock key validation logic
    if token != "your-mock-key":
        raise HTTPException(status_code=401, detail="Invalid API key")
    return token

class YourRequestModel(BaseModel):
    """Define your request schema."""
    # Add fields here
    pass

@router.post("/your/endpoint")
def your_endpoint(request: YourRequestModel, token: str = Depends(verify_api_key)):
    """
    Your mock endpoint implementation.
    
    Document what this endpoint does and how it differs from the real service.
    """
    # Implement your mock logic here
    return {"status": "success"}
```

### 2. Export the Router

Add your router to `app/mocks/__init__.py`:

```python
from app.mocks.openai_ollama import router as openai_router
from app.mocks.pinecone_mock import router as pinecone_router  # Add this

__all__ = ["openai_router", "pinecone_router"]  # Add to exports
```

### 3. Mount in Main App

In `app/main.py`, import and mount your router:

```python
from app.mocks import openai_router, pinecone_router

# Mount the routers
app.include_router(openai_router, tags=["OpenAI Mock"])
app.include_router(pinecone_router, tags=["Pinecone Mock"])  # Add this
```

### 4. Document Your Mock

Add documentation to this README:

- What service does it mock?
- What endpoints are available?
- What are the mock credentials?
- Any special configuration needed?

## Best Practices

1. **Authentication**: Always implement mock authentication to simulate real-world scenarios
2. **Error Handling**: Include realistic error responses
3. **Logging**: Add debug logging to help with testing
4. **Documentation**: Document all endpoints with clear docstrings
5. **Type Safety**: Use Pydantic models for request/response validation
6. **Modularity**: Keep each mock service independent and self-contained

## Example Mock Services to Add

- **Pinecone**: Mock vector database operations
- **Anthropic**: Mock Claude API
- **Cohere**: Mock Cohere API
- **Hugging Face**: Mock inference endpoints
- **ChromaDB**: Mock vector database
- **Weaviate**: Mock vector database

## Testing Your Mock

After adding a new mock service:

1. Update the Makefile if needed
2. Test with curl or the client scripts
3. Verify authentication works
4. Check error handling
5. Update README.md with usage examples
