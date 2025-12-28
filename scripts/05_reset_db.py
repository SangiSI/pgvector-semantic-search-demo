dropdb vectordb || true
createdb vectordb
uv run python scripts/10_init_db.py
