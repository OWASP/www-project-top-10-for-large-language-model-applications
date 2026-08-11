FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir aiohttp

# Copy agent files
COPY agent.py /app/
COPY mcp_registry.json /app/
COPY mcp_registry_poisoned.json /app/

EXPOSE 5050

CMD ["python", "agent.py"]
