"""RAG Engine implementation.

This module implements the RAG logic, acting as the "Application Server" in the architecture.
It communicates with the Mock OpenAI API and Mock Pinecone API to perform Retrieval Augmented Generation.
"""

import os
from typing import Any, Dict, List, Optional

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Configuration for internal service calls
# In a real microservices setup, these would be different hosts.
# Here we point to localhost:8000 where the mocks are running.
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
OPENAI_BASE_URL = f"{API_BASE_URL}/v1"
PINECONE_BASE_URL = f"{API_BASE_URL}/pinecone"

# Mock Credentials
OPENAI_API_KEY = "sk-mock-key"
PINECONE_API_KEY = "bar"


class ChatCompletionRequest(BaseModel):
    """Request model for chat completions."""
    model: str
    messages: List[Dict[str, Any]]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    stream: Optional[bool] = False


@router.post("/rag/v1/chat/completions")
async def rag_chat(request: ChatCompletionRequest) -> Any:
    """RAG Chat Endpoint.
    
    Orchestrates the RAG flow:
    1. Embed user query (via Mock OpenAI)
    2. Retrieve context (via Mock Pinecone)
    3. Augment prompt
    4. Generate response (via Mock OpenAI)
    """
    print(f"DEBUG: RAG Request received for model {request.model}")
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        # 1. Extract last user message
        last_user_message = next(
            (m["content"] for m in reversed(request.messages) if m["role"] == "user"), 
            None
        )
        
        context_text = ""
        
        debug_info = []
        
        if last_user_message:
            try:
                # 2. Generate Embedding
                print("DEBUG: Generating embedding...")
                embedding_response = await client.post(
                    f"{OPENAI_BASE_URL}/embeddings",
                    headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                    json={
                        "model": "nomic-embed-text", # Use a default embedding model
                        "input": last_user_message
                    }
                )
                embedding_response.raise_for_status()
                embedding = embedding_response.json()["data"][0]["embedding"]
                
                # 3. Query Mock Pinecone
                print("DEBUG: Querying Vector DB...")
                query_response = await client.post(
                    f"{PINECONE_BASE_URL}/query",
                    headers={"Api-Key": PINECONE_API_KEY},
                    json={
                        "vector": embedding,
                        "topK": 3,
                        "includeMetadata": True
                    }
                )
                query_response.raise_for_status()
                results = query_response.json()
                
                # 4. Construct Context
                matches = results.get("matches", [])
                print(f"DEBUG: Found {len(matches)} matches")
                
                debug_info.append(f"Query: {last_user_message}")
                debug_info.append(f"Retrieved {len(matches)} chunks:")
                
                for i, match in enumerate(matches):
                    metadata = match.get("metadata", {})
                    text = metadata.get("text", "")
                    score = match.get("score", 0.0)
                    source = metadata.get("source", "unknown")
                    
                    print(f"  - Score: {score:.4f} | Content: {text[:50]}...")
                    
                    debug_info.append(f"\n[Chunk {i+1}] Score: {score:.4f} | Source: {os.path.basename(source)}")
                    debug_info.append(f"Content: {text[:150]}..." if len(text) > 150 else f"Content: {text}")
                    
                    if text:
                        context_text += f"- {text}\n"
                        
            except Exception as e:
                print(f"WARNING: RAG retrieval failed: {e}")
                # Proceed without context on error
        
        # 5. Augment Prompt
        messages = list(request.messages) # Copy
        if context_text:
            print("DEBUG: Augmenting prompt with context")
            system_message = {
                "role": "system", 
                "content": f"You are a helpful assistant. Use the following context to answer the user's question:\n\nContext:\n{context_text}"
            }
            
            # Insert context
            if messages and messages[0]["role"] == "system":
                messages[0]["content"] += f"\n\nAdditional Context:\n{context_text}"
            else:
                messages.insert(0, system_message)
        
        # 6. Generate Response
        print("DEBUG: Generating response...")
        try:
            chat_response = await client.post(
                f"{OPENAI_BASE_URL}/chat/completions",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                json={
                    "model": request.model,
                    "messages": messages,
                    "temperature": request.temperature,
                    "max_tokens": request.max_tokens,
                    "top_p": request.top_p,
                    "stream": request.stream
                }
            )
            chat_response.raise_for_status()
            response_data = chat_response.json()
            
            # Append Debug Info to Content
            if debug_info and "choices" in response_data and response_data["choices"]:
                debug_text = "\n\n" + "="*40 + "\n🔎 RAG DEBUG INFO\n" + "="*40 + "\n"
                debug_text += "\n".join(debug_info)
                debug_text += "\n" + "="*40
                
                # Append to the first choice's content
                if "message" in response_data["choices"][0]:
                    content = response_data["choices"][0]["message"].get("content", "")
                    response_data["choices"][0]["message"]["content"] = content + debug_text
            
            return response_data
            
        except httpx.HTTPStatusError as e:
            print(f"ERROR: Upstream API error: {e.response.text}")
            raise HTTPException(status_code=e.response.status_code, detail=f"Upstream error: {e.response.text}")
        except Exception as e:
            print(f"ERROR: Generation failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))
