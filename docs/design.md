# Design

This repo demonstrates vector similarity search using PostgreSQL + pgvector.

## Data model
- `documents`: metadata for each source document
- `chunks`: chunked text + embedding vector (unit of retrieval)

This structure is RAG-friendly:
1) chunk documents
2) embed chunks
3) retrieve top-k chunks for a query
4) pass retrieved text to an LLM prompt
