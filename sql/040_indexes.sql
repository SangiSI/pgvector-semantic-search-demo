-- Optional: add an ANN index when you move to real embeddings & larger data.
-- Choose ops class based on distance metric:
--  - L2: vector_l2_ops
--  - cosine: vector_cosine_ops
--  - inner product: vector_ip_ops

-- Example (cosine):
-- CREATE INDEX IF NOT EXISTS chunks_embedding_hnsw
-- ON chunks
-- USING hnsw (embedding vector_cosine_ops);
