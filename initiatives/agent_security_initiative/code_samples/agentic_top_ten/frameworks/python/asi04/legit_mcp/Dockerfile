FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir aiohttp

# Copy server
COPY server.py /app/

EXPOSE 5001

CMD ["python", "server.py"]
