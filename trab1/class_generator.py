import os
from example_generator import generate_random_value

def generate_class(class_name, class_content, directory):
    # Escreve a classe em um arquivo .py na pasta correspondente
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/{class_name}.py", "w") as file:
        file.write(class_content)

def generate_entity_class(table_name, column_names):
    # Cria a classe de entidade
    class_name = table_name.capitalize()
    class_content = f"class {class_name}:\n    def __init__(self, {', '.join(column_names)}):\n"
    class_content += '\n'.join([f"        self.{column} = {column}" for column in column_names])
    
    generate_class(class_name, class_content, 'entities')

def generate_dao_class(table_name):
    # Cria a classe DAO específica que herda de GenericDao
    class_name = f"{table_name.capitalize()}Dao"
    class_content = f"from generic_dao import GenericDao\n\nclass {class_name}(GenericDao):\n    def __init__(self, db_path):\n        super().__init__(db_path, '{table_name}')\n"
    
    generate_class(class_name, class_content, 'daos')

def generate_example_class(table_name, column_names, column_types, current_id):
    # Cria a classe de exemplo
    class_name = f"{table_name.capitalize()}Exemplo"
    class_content = f"class {class_name}:\n    def __init__(self):\n"
    for column, column_type in zip(column_names, column_types):
        if column == 'id':
            class_content += f"        self.{column} = {current_id}\n"
        else:
            random_value = generate_random_value(column_type)
            if column_type == "TEXT":
                random_value = f'{random_value}'
            class_content += f"        self.{column} = {random_value}\n"
    
    generate_class(class_name, class_content, 'examples')

