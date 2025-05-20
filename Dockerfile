FROM python:3.13-slim AS base

FROM base AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.4.9 /uv /usr/local/bin/uv
RUN chmod +x /usr/local/bin/uv

WORKDIR /app

COPY uv.lock pyproject.toml /app/

RUN python -m venv /app/.venv

RUN --mount=type=cache,target=/root/.cache/uv \
    /app/.venv/bin/python -m pip install --upgrade pip \
    && /app/.venv/bin/pip install uv \
    && /app/.venv/bin/uv sync --frozen --no-install-project --no-dev


COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    /app/.venv/bin/uv sync --frozen --no-dev

FROM base

COPY --from=builder /usr/local/bin/uv /usr/local/bin/uv
RUN chmod +x /usr/local/bin/uv

COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:/usr/local/bin:$PATH"

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]