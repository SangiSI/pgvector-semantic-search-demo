## RAG Next Steps

This repository intentionally focuses on pgvector integration and retrieval mechanics.
To evolve it into a **production-grade RAG pipeline**, the following extensions would be required:

1. **Embedding generation**
   - Integrate a real embedding model (e.g. 384 / 768 / 1536 dimensions)
   - Support local or hosted embedding backends

2. **Schema update**
   - Update the embedding column to `VECTOR(<dim>)`
   - Re-ingest data with real embeddings

3. **Approximate Nearest Neighbor (ANN) indexing**
   - Add HNSW or IVFFlat indexes for scalable retrieval
   - Tune index parameters based on dataset size and latency targets

4. **Retrieval API**
   - Expose search via a lightweight API (e.g. FastAPI `/search`)
   - Encapsulate SQL queries behind a service boundary

5. **Evaluation & monitoring**
   - Add offline metrics (precision@k, recall@k, MRR)
   - Track online metrics (latency, throughput)

These steps are deliberately out of scope for this repository to keep the focus on
clarity, correctness, and database-first vector search fundamentals.
