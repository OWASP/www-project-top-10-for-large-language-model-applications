FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY vulnerable_agent.py .
COPY protected_agent.py .

# Run the vulnerable agent by default.
# Override with: docker run ... python protected_agent.py
CMD ["python", "vulnerable_agent.py"]
