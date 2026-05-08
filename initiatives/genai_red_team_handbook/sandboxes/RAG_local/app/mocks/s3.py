from fastapi import APIRouter, Request, HTTPException, Header
import os
from typing import Annotated

router = APIRouter()

DATA_DIR = "data"

@router.put("/{bucket_name}/{object_key:path}")
async def put_object(
    bucket_name: str,
    object_key: str,
    request: Request,
    api_key: Annotated[str | None, Header()] = None
):
    if api_key != "foobar":
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # For this mock, we only support the 'documents' bucket mapping to data/documents
    # Or we can just treat the bucket as a folder in data/
    # Let's follow the plan: if bucket is 'documents', save to data/documents
    
    if bucket_name == "documents":
        target_dir = os.path.join(DATA_DIR, "documents")
    else:
        # Optional: support other buckets or just default to creating a folder
        target_dir = os.path.join(DATA_DIR, bucket_name)

    os.makedirs(target_dir, exist_ok=True)
    
    # Handle nested keys (folders)
    file_path = os.path.join(target_dir, object_key)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    try:
        body = await request.body()
        with open(file_path, "wb") as f:
            f.write(body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")
        
    return {"message": "Object uploaded successfully", "key": object_key, "bucket": bucket_name}
