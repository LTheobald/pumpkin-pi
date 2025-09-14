FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY . /app

# Install project in editable mode with dev extras
RUN pip install --upgrade pip \
    && pip install -e .[dev]

# Default command keeps container open for interactive work
CMD ["bash"]
