INSERT INTO documents (source, title) VALUES
  ('demo', 'Tiny demo doc');

INSERT INTO chunks (document_id, chunk_index, content, embedding) VALUES
  (1, 0, '5G network optimization', '[1,2,3]'),
  (1, 1, 'AI driven RAN analytics', '[2,3,4]'),
  (1, 2, 'PostgreSQL vector similarity search with pgvector', '[9,9,9]');
