#!/bin/sh
uv run python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
