# RAG Next Steps

To upgrade this repo into a real RAG pipeline:

1. Use a real embedding model (384/768/1536 dims)
2. Update schema: `embedding VECTOR(<dim>)`
3. Add ANN index (HNSW / IVFFlat)
4. Add an API (FastAPI /search)
5. Add evaluation (precision@k, MRR, latency)
