import os
from pathlib import Path

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = ROOT / "sql"

ADMIN_DB_URL = os.getenv("PGVECTOR_ADMIN_DB_URL", "postgresql://postgres@localhost:5432/postgres")
TARGET_DB_URL = os.getenv("PGVECTOR_DB_URL", "postgresql://postgres@localhost:5432/vectordb")

def run_sql(conn, sql_path: Path) -> None:
    sql = sql_path.read_text(encoding="utf-8")
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    print(f"Ran {sql_path.name}")

def ensure_db_exists() -> None:
    dbname = "vectordb"
    conn = psycopg2.connect(ADMIN_DB_URL)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (dbname,))
        exists = cur.fetchone() is not None
        if not exists:
            cur.execute(f"CREATE DATABASE {dbname};")
            print("Created database vectordb")
        else:
            print("ℹ️ Database vectordb already exists")
    conn.close()

def main() -> None:
    ensure_db_exists()
    conn = psycopg2.connect(TARGET_DB_URL)

    run_sql(conn, SQL_DIR / "010_extensions.sql")
    run_sql(conn, SQL_DIR / "020_schema.sql")
    run_sql(conn, SQL_DIR / "030_seed.sql")

    conn.close()
    print("DB initialized")

if __name__ == "__main__":
    main()
