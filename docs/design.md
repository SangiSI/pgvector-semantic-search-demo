## Design

This repository demonstrates **vector similarity search** using **PostgreSQL + pgvector**, with a data model intentionally structured to mirror real-world RAG systems.

### Data model

- **`documents`**  
  Stores metadata for each source document (origin, title, identifiers).

- **`chunks`**  
  Stores chunked text content along with its embedding vector.  
  This table is the **unit of retrieval** during similarity search.

### Retrieval pattern (RAG-friendly)

The design follows a standard Retrieval-Augmented Generation (RAG) workflow:

1. Split documents into smaller text chunks  
2. Generate embeddings for each chunk  
3. Retrieve top-k most similar chunks for a query  
4. Pass retrieved text to an LLM prompt (outside the scope of this repo)

This separation keeps the schema simple, extensible, and compatible with both
SQL-first querying and downstream LLM pipelines.
