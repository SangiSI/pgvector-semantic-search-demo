# pgvector Semantic Search Demo (PostgreSQL)

A clean learning/demo repository showing how to use PostgreSQL + pgvector for vector similarity search.
Structured like a real project and easy to extend into RAG or ML pipelines.

## What this repo demonstrates
- pgvector extension setup
- RAG-friendly schema (documents + chunks + embeddings)
- Similarity search queries in SQL
- Python ingestion + search scripts

## Prerequisites
- Postgres.app running locally (macOS)
- `psql` available in terminal
- `uv` installed

## Quickstart (uv)

### 1) Create venv and install dependencies
```bash
uv venv
uv pip install psycopg2-binary python-dotenv
uv lock

### 2) Initialize database + schema
```bash
uv run python scripts/10_init_db.py

### 3) Run a similarity query (SQL)
```bash
psql -d vectordb -f sql/050_queries.sql

### 4) Ingest more demo chunks (Python)
```bash
uv run python scripts/20_ingest_demo.py

### 5) Search via Python
```bash
uv run python scripts/30_search_demo.py

## Notes
- Embedding dimension is VECTOR(3) for a tiny demo.
- For real usage, switch to 384/768/1536 and add an ANN index.

### 8) Run the full flow (sanity test)

- Make sure Postgres.app is running.

- Then:

```bash
uv run python scripts/00_check_connection.py
uv run python scripts/10_init_db.py
psql -d vectordb -f sql/050_queries.sql
uv run python scripts/20_ingest_demo.py
uv run python scripts/30_search_demo.py
