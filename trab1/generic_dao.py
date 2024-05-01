import sqlite3
from class_import import import_class

class GenericDao:
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name

    #Executa uma consulta genérica
    def _execute_query(self, query, params=()):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor

    #Obtém todos os dados usando a consulta genérica
    def get_all(self):
        cursor = self._execute_query(f"SELECT * FROM {self.table_name}")
        return cursor.fetchall()

    #Obtém um dado pelo id usando a consulta genérica
    def get_by_id(self, id):
        cursor = self._execute_query(f"SELECT * FROM {self.table_name} WHERE id = ?", (id,))
        record = cursor.fetchone()
        EntityClass = import_class(f"entities.{self.table_name.capitalize()}", self.table_name.capitalize())
        return EntityClass(*record) if record else None

    #Realiza a inserção de um novo registro
    def insert(self, entity):
        entity_dict = vars(entity)
        columns = ', '.join(entity_dict.keys())
        placeholders = ', '.join('?' for _ in entity_dict)
        sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self._execute_query(sql, list(entity_dict.values()))

    #Realiza a atualização de um o registro selecionado
    def update(self, entity, id):
        entity_dict = vars(entity)
        updateable_columns = [key for key in entity_dict.keys() if key != 'id']
        columns = ', '.join(f"{key} = ?" for key in updateable_columns)
        values = [entity_dict[key] for key in updateable_columns]
        values.append(id)
        sql = f"UPDATE {self.table_name} SET {columns} WHERE id = ?"
        self._execute_query(sql, values)

    #Realiza a exclusão de um registro selecionado
    def delete(self, id):
        self._execute_query(f"DELETE FROM {self.table_name} WHERE id = ?", (id,))
