import os
import psycopg2

DB_URL = os.getenv("PGVECTOR_DB_URL", "postgresql://postgres@localhost:5432/vectordb")

DEMO_DOC = {
    "source": "demo",
    "title": "Demo ingestion doc",
    "chunks": [
        ("Semantic search with pgvector", [3, 3, 3]),
        ("Vector search inside Postgres", [4, 4, 4]),
        ("RAG: retrieve top-k chunks then prompt an LLM", [5, 5, 5]),
    ],
}

def main() -> None:
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO documents (source, title) VALUES (%s, %s) RETURNING id;",
        (DEMO_DOC["source"], DEMO_DOC["title"]),
    )
    doc_id = cur.fetchone()[0]

    for idx, (text, emb) in enumerate(DEMO_DOC["chunks"]):
        cur.execute(
            """
            INSERT INTO chunks (document_id, chunk_index, content, embedding)
            VALUES (%s, %s, %s, %s);
            """,
            (doc_id, idx, text, emb),
        )

    conn.commit()
    cur.close()
    conn.close()
    print(f"Ingested document_id={doc_id} with {len(DEMO_DOC['chunks'])} chunks")

if __name__ == "__main__":
    main()
