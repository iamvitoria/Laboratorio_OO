import sqlite3

def execute_query(db_path, query, params=()):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor

def get_last_id(db_path, table_name):
    cursor = execute_query(db_path, f"SELECT MAX(id) FROM {table_name}")
    last_id = cursor.fetchone()[0]
    return last_id if last_id is not None else 0

def get_table_names(db_path):
    cursor = execute_query(db_path, "SELECT name FROM sqlite_master WHERE type='table';")
    return [name[0] for name in cursor.fetchall()]

def get_column_info(db_path, table_name):
    cursor = execute_query(db_path, f"PRAGMA table_info({table_name});")
    return cursor.fetchall()

def get_column_names(db_path, table_name):
    columns = get_column_info(db_path, table_name)
    return [column[1] for column in columns]

def get_column_types(db_path, table_name):
    columns = get_column_info(db_path, table_name)
    return [column[2] for column in columns]