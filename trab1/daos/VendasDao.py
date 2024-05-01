from generic_dao import GenericDao

class VendasDao(GenericDao):
    def __init__(self, db_path):
        super().__init__(db_path, 'VENDAS')
