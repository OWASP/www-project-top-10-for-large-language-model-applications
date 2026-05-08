"""Mock Pinecone API implementation using ChromaDB as the backend.

This module provides a FastAPI router that mimics a subset of the Pinecone API,
routing requests to a local ChromaDB instance.
"""

import os
from typing import Any, Dict, List, Optional

import chromadb
from chromadb.config import Settings
from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel

# Initialize ChromaDB client
# We use a persistent client to store data locally
chroma_client = chromadb.PersistentClient(path="./data/chromadb")


def get_collection():
    """Get or create the default collection."""
    return chroma_client.get_or_create_collection(name="default_collection")


router = APIRouter()


def verify_api_key(api_key: str = Header(..., alias="Api-Key")) -> str:
    """Mock API key verification for Pinecone.

    Args:
        api_key: The API key from the 'Api-Key' header.

    Returns:
        str: The validated API key.

    Raises:
        HTTPException: If the API key is invalid.
    """
    if api_key != "bar":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key


class Vector(BaseModel):
    id: str
    values: List[float]
    metadata: Optional[Dict[str, Any]] = None


class UpsertRequest(BaseModel):
    vectors: List[Vector]
    namespace: Optional[str] = None


class QueryRequest(BaseModel):
    vector: List[float]
    topK: int = 10
    namespace: Optional[str] = None
    includeMetadata: bool = False
    includeValues: bool = False


@router.post("/vectors/upsert")
def upsert_vectors(
    request: UpsertRequest, token: str = Depends(verify_api_key)
) -> Dict[str, int]:
    """Mock Pinecone upsert endpoint.

    Stores vectors in the local ChromaDB collection.
    """
    collection = get_collection()
    
    ids = [v.id for v in request.vectors]
    embeddings = [v.values for v in request.vectors]
    metadatas = [v.metadata or {} for v in request.vectors]
    
    # ChromaDB requires documents, but for pure vector search we can use empty strings
    # or just not provide them if the version supports it. 
    # For simplicity, we'll provide empty strings as documents if not provided in metadata
    documents = [str(m.get("text", "")) for m in metadatas]

    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents
    )

    return {"upsertedCount": len(ids)}


@router.post("/query")
def query_vectors(
    request: QueryRequest, token: str = Depends(verify_api_key)
) -> Dict[str, Any]:
    """Mock Pinecone query endpoint.

    Queries the local ChromaDB collection.
    """
    collection = get_collection()
    
    results = collection.query(
        query_embeddings=[request.vector],
        n_results=request.topK,
        include=["metadatas", "distances", "documents"] if request.includeMetadata else ["distances"]
    )
    
    matches = []
    if results["ids"]:
        # Chroma returns list of lists (one per query vector)
        ids = results["ids"][0]
        distances = results["distances"][0] if results["distances"] else []
        metadatas = results["metadatas"][0] if results["metadatas"] else []
        
        for i, id_ in enumerate(ids):
            match = {
                "id": id_,
                "score": 1.0 - distances[i] if i < len(distances) else 0.0, # Chroma returns distance, Pinecone returns score (similarity)
            }
            if request.includeMetadata and i < len(metadatas):
                match["metadata"] = metadatas[i]
            matches.append(match)

    return {
        "matches": matches,
        "namespace": request.namespace or ""
    }
