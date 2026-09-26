# ── Build stage ───────────────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies into a clean prefix
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ── Runtime stage ─────────────────────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application files
COPY main.py knowledge_base.py index.html ./
COPY static/ ./static/

# Render injects $PORT at runtime — default to 8000 for local docker run
ENV PORT=8000

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}
