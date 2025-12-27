import os
import psycopg2

DB_URL = os.getenv("PGVECTOR_DB_URL", "postgresql://postgres@localhost:5432/vectordb")

def main() -> None:
    query_embedding = [2, 2, 2]

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT d.title, c.chunk_index, c.content, (c.embedding <-> %s) AS distance
        FROM chunks c
        JOIN documents d ON d.id = c.document_id
        ORDER BY c.embedding <-> %s
        LIMIT 5;
        """,
        (query_embedding, query_embedding),
    )

    for title, chunk_index, content, distance in cur.fetchall():
        print(f"- {distance:.4f} | {title} | chunk={chunk_index} | {content}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
