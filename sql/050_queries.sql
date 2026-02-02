-- Demo vector similarity search using pgvector (L2 distance)
-- Retrieves the top-k most similar chunks for a given query embedding

SELECT
  c.id,
  d.title,
  c.chunk_index,
  c.content,
  (c.embedding <-> '[2,2,2]') AS l2_distance
FROM chunks c
JOIN documents d ON d.id = c.document_id
ORDER BY c.embedding <-> '[2,2,2]'
LIMIT 5;
