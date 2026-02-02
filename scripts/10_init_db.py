"""
Author: Sangam Kumar Singh
Source: https://github.com/SangiSI/pgvector-semantic-search-demo
License: MIT

Database initialization script for the pgvector semantic search demo.

This script:
- ensures the target database exists
- enables required extensions
- creates schema objects
- seeds sample data
"""

import os
from pathlib import Path

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = ROOT / "sql"

ADMIN_DB_URL = os.getenv(
    "PGVECTOR_ADMIN_DB_URL",
    "postgresql://postgres@localhost:5432/postgres",
)
TARGET_DB_URL = os.getenv(
    "PGVECTOR_DB_URL",
    "postgresql://postgres@localhost:5432/vectordb",
)


def run_sql(conn, sql_path: Path) -> None:
    """
    Execute a SQL file against an open PostgreSQL connection.

    Args:
        conn: Active psycopg2 connection.
        sql_path (Path): Path to the SQL file to execute.
    """
    sql = sql_path.read_text(encoding="utf-8")
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    print(f"Ran {sql_path.name}")


def ensure_db_exists() -> None:
    """
    Ensure that the target database exists.

    Connects to the admin database and creates the target database
    if it does not already exist.
    """
    dbname = "vectordb"
    conn = psycopg2.connect(ADMIN_DB_URL)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    with conn.cursor() as cur:
        cur.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s;",
            (dbname,),
        )
        exists = cur.fetchone() is not None

        if not exists:
            cur.execute(f"CREATE DATABASE {dbname};")
            print("Created database vectordb")
        else:
            print("ℹ️ Database vectordb already exists")

    conn.close()


def main() -> None:
    """
    Initialize the pgvector demo database.

    Runs database creation (if needed), installs extensions,
    creates schema objects, and seeds demo data.
    """
    ensure_db_exists()
    conn = psycopg2.connect(TARGET_DB_URL)

    run_sql(conn, SQL_DIR / "010_extensions.sql")
    run_sql(conn, SQL_DIR / "020_schema.sql")
    run_sql(conn, SQL_DIR / "030_seed.sql")

    conn.close()
    print("DB initialized")


if __name__ == "__main__":
    main()
