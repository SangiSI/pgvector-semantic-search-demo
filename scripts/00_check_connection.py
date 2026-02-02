"""
Author: Sangam Kumar Singh
Source: https://github.com/SangiSI/pgvector-semantic-search-demo
License: MIT

Minimal connectivity check for a PostgreSQL instance used in pgvector demos.
"""

import os
import psycopg2

DB_URL = os.getenv(
    "PGVECTOR_DB_URL",
    "postgresql://postgres@localhost:5432/postgres",
)


def main() -> None:
    """
    Verify connectivity to the PostgreSQL database.

    Connects using the database URL provided via the PGVECTOR_DB_URL
    environment variable (or a local default), executes a simple
    version query, and prints the result.

    This script is intended as a sanity check before running
    schema initialization or ingestion steps.
    """
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    cur.execute("SELECT version();")
    print(cur.fetchone()[0])

    cur.close()
    conn.close()

    print("Connection OK")


if __name__ == "__main__":
    main()
