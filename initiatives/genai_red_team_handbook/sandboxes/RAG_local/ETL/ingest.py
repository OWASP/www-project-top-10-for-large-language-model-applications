"""PDF Ingestion Script

This script reads a PDF file, extracts text, chunks it recursively, generates embeddings (using Ollama),
and upserts the vectors into the mock Pinecone API.
"""

import argparse
import os
import sys
from typing import List

import requests
from pypdf import PdfReader
from openai import OpenAI

# Configuration
MOCK_API_URL = "http://localhost:8000"
API_KEY = "bar"
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
EMBEDDING_MODEL = "nomic-embed-text"  # Use the same model as chat, or 'nomic-embed-text' if available

client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def recursive_chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Recursive text chunking."""
    separators = ["\n\n", "\n", " ", ""]
    
    def _merge(splits: List[str], separator: str, chunk_size: int, overlap: int) -> List[str]:
        docs = []
        current_doc = []
        current_len = 0
        
        for split in splits:
            split_len = len(split)
            sep_len = len(separator) if current_doc else 0
            
            # If adding the next split exceeds the chunk size
            if current_len + sep_len + split_len > chunk_size:
                if current_doc:
                    doc = separator.join(current_doc)
                    docs.append(doc)
                    
                    # Handle overlap: remove from the beginning until we are under the overlap limit
                    # This is a simplified overlap strategy
                    while current_len > overlap:
                        if not current_doc:
                            break
                        removed = current_doc.pop(0)
                        current_len -= len(removed)
                        if current_doc:
                            current_len -= len(separator)
                    
                    # If after popping we are still too big (unlikely if split < chunk_size), clear
                    if current_len + sep_len + split_len > chunk_size:
                        current_doc = []
                        current_len = 0

            current_doc.append(split)
            current_len += len(split) + (len(separator) if len(current_doc) > 1 else 0)
            
        if current_doc:
            docs.append(separator.join(current_doc))
            
        return docs

    def _split_text(text: str, separators: List[str]) -> List[str]:
        # Find the appropriate separator
        separator = separators[-1]
        new_separators = []
        for i, s in enumerate(separators):
            if s == "":
                separator = ""
                break
            if s in text:
                separator = s
                new_separators = separators[i+1:]
                break
        
        # Split
        if separator:
            splits = text.split(separator)
        else:
            splits = list(text) # Character split
            
        # Process splits
        good_splits = []
        for s in splits:
            if len(s) < chunk_size:
                good_splits.append(s)
            else:
                if new_separators:
                    good_splits.extend(_split_text(s, new_separators))
                else:
                    good_splits.append(s) # Force keep if no more separators
        
        # Merge
        return _merge(good_splits, separator, chunk_size, overlap)

    return _split_text(text, separators)


def get_embedding(text: str) -> List[float]:
    """Generate embedding using Ollama."""
    try:
        response = client.embeddings.create(model=EMBEDDING_MODEL, input=text)
        return response.data[0].embedding
    except Exception as e:
        print(f"Error generating embedding: {e}")
        # Return a dummy embedding if generation fails (for testing)
        # In production, you'd want to fail or retry
        return [0.0] * 768 # nomic-embed-text dimension


def upsert_to_pinecone(id: str, values: List[float], metadata: dict):
    """Upsert vector to mock Pinecone API."""
    url = f"{MOCK_API_URL}/pinecone/vectors/upsert"
    headers = {"Api-Key": API_KEY, "Content-Type": "application/json"}
    payload = {
        "vectors": [
            {
                "id": id,
                "values": values,
                "metadata": metadata
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Failed to upsert {id}: {response.text}")
    else:
        print(f"Successfully upserted {id}")


def main():
    parser = argparse.ArgumentParser(description="Ingest PDF into Mock Vector DB")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"File not found: {args.pdf_path}")
        sys.exit(1)

    print(f"Extracting text from {args.pdf_path}...")
    text = extract_text_from_pdf(args.pdf_path)
    
    print("Chunking text recursively...")
    chunks = recursive_chunk_text(text)
    print(f"Generated {len(chunks)} chunks.")

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}...")
        embedding = get_embedding(chunk)
        
        # Upsert
        upsert_to_pinecone(
            id=f"doc_{os.path.basename(args.pdf_path)}_{i}",
            values=embedding,
            metadata={"text": chunk, "source": args.pdf_path}
        )

    print("Ingestion complete!")


if __name__ == "__main__":
    main()
