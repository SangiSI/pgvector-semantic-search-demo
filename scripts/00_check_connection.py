import os
import psycopg2

DB_URL = os.getenv("PGVECTOR_DB_URL", "postgresql://postgres@localhost:5432/postgres")

def main() -> None:
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone()[0])
    cur.close()
    conn.close()
    print("Connection OK")

if __name__ == "__main__":
    main()
