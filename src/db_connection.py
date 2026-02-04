import sqlite3
import pandas as pd
from pathlib import Path

def get_db_connection(db_path: str):
    """
    Create and return a SQLite database connection
    """
    return sqlite3.connect(db_path)


def fetch_table_as_df(db_path: str, table_name: str) -> pd.DataFrame:
    """
    Fetch a table from SQLite DB and return as pandas DataFrame
    """
    conn = get_db_connection(db_path)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def list_tables(db_path: str):
    """
    List all tables available in the SQLite database
    """
    conn = get_db_connection(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]
