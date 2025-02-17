FROM python:3.12-slim

# Create a non-root user and group for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set the working directory in the container
WORKDIR /app

# Copy only requirements file first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install -qq --no-cache-dir --quiet -r requirements.txt > /dev/null 2>&1

# Install pandoc and texlive using apt-get
ENV DEBIAN_FRONTEND=noninteractive
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    apt-get update -qq && \
    apt-get install -qq -y \
    pandoc \
    texlive-latex-base \
    texlive-latex-extra \
    > /dev/null 2>&1 && \
    apt-get clean -qq && \
    rm -rf /var/lib/apt/lists/*

# Copy the application source code into the container
COPY . /app

# Set up permissions for the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Define the default command to run the app
CMD ["python", "ai_recruiter.py"]
