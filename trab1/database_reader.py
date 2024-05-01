import sqlite3

#Executa qualquer consulta
def execute_query(db_path, query, params=()):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor

#Obtém o último id de registro
def get_last_id(db_path, table_name):
    cursor = execute_query(db_path, f"SELECT MAX(id) FROM {table_name}")
    last_id = cursor.fetchone()[0]
    return last_id if last_id is not None else 0

#Obtém os nomes de cada tabela
def get_table_names(db_path):
    cursor = execute_query(db_path, "SELECT name FROM sqlite_master WHERE type='table';")
    return [name[0] for name in cursor.fetchall()]

#Obtém algumas informações de cada coluna
def get_column_info(db_path, table_name):
    cursor = execute_query(db_path, f"PRAGMA table_info({table_name});")
    return cursor.fetchall()

#Obtém os nomes de cada coluna
def get_column_names(db_path, table_name):
    columns = get_column_info(db_path, table_name)
    return [column[1] for column in columns]

#Obtém os tipos de cada coluna
def get_column_types(db_path, table_name):
    columns = get_column_info(db_path, table_name)
    return [column[2] for column in columns]