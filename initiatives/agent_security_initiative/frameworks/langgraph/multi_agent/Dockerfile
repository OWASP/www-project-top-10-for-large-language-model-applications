FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    sqlite3 \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright dependencies
RUN pip install playwright && \
    playwright install --with-deps chromium

# Install poetry and configure it
RUN pip install poetry && \
    poetry config virtualenvs.create false

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Install dependencies directly with poetry
RUN poetry install --no-interaction --no-ansi --no-root

# Copy application code
COPY . .

# Create data directory for SQLite database
RUN mkdir -p /data

# Initialize database with sample data
RUN python create_patient_db.py

# Default command
CMD ["python", "get_patients_fit_for_als_trials.py"]
