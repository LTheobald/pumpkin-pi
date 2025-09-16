# syntax=docker/dockerfile:1.7-labs
ARG PYTHON_VERSION=3.12
FROM --platform=$BUILDPLATFORM python:${PYTHON_VERSION}-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y gcc build-essential git && rm -rf /var/lib/apt/lists/*

# deps
FROM base AS deps
WORKDIR /app
COPY pyproject.toml uv.lock** ./
RUN pip install uv && uv sync --frozen

# runnable
FROM base AS runtime
WORKDIR /app
COPY --from=deps /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY src/ ./src/
CMD ["python","-m","your_pkg.app"]
