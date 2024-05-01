from generic_dao import GenericDao

class ClientesDao(GenericDao):
    def __init__(self, db_path):
        super().__init__(db_path, 'CLIENTES')
