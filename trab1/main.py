from database_reader import get_last_id, get_table_names, get_column_names, get_column_types
from class_generator import generate_dao_class, generate_entity_class, generate_example_class
from class_import import import_class

def main():
    db_path = 'loja.db'
    table_names = get_table_names(db_path)

    for table in table_names:
        column_names = get_column_names(db_path, table)
        column_types = get_column_types(db_path, table)
        current_id = get_last_id(db_path, table) + 1

        # Gera as classes e escreve em arquivos .py nas pastas correspondentes
        generate_entity_class(table, column_names)
        generate_dao_class(table)
        generate_example_class(table, column_names, column_types, current_id)

    while True:
        print("Selecione uma tabela:")
        for i, table in enumerate(table_names):
            print(f"{i+1}. {table}")
        print(f"{len(table_names)+1}. Sair")
        
        try:
            table_choice = int(input("Escolha: ")) - 1
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if table_choice == len(table_names):
            break

        if table_choice < 0 or table_choice >= len(table_names):
            print("Por favor, escolha um número da lista.")
            continue

        table = table_names[table_choice]
        column_names = get_column_names(db_path, table)
        column_types = get_column_types(db_path, table)

        # Importa as classes criadas dinamicamente
        EntityClass = import_class(f"entities.{table.capitalize()}", table.capitalize())
        DaoClass = import_class(f"daos.{table.capitalize()}Dao", f"{table.capitalize()}Dao")
        ExampleClass = import_class(f"examples.{table.capitalize()}Exemplo", f"{table.capitalize()}Exemplo")

        dao = DaoClass(db_path)

        while True:
            print(f"\nTabela selecionada: {table}")
            print("1. Adicionar registro")
            print("2. Atualizar registro")
            print("3. Excluir registro")
            print("4. Listar todos os registros")
            print("5. Adicionar registro de exemplo")
            print("6. Voltar")
            
            try:
                action_choice = int(input("Escolha: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if action_choice == 6:
                break

            elif action_choice == 1:
                # Adicionar registro
                entity_values = [current_id]  # O primeiro valor é o ID
                for column in column_names:
                    if column != 'id':  # Não permitir a entrada do ID
                        value = input(f"Digite o valor para {column}: ")
                        entity_values.append(value)
                entity = EntityClass(*entity_values)
                dao.insert(entity)
                current_id += 1  # Incrementa o ID para o próximo registro

            elif action_choice == 2:
                # Atualizar registro
                id = int(input("Digite o ID do registro que deseja atualizar: "))
                entity = dao.get_by_id(id)
                if entity is None:
                    print("Registro não encontrado.")
                    continue
                print(f"Registro atual: {vars(entity)}")  # Mostra o registro atual de forma mais legível
                print("Selecione o campo que deseja atualizar:")
                updateable_columns = [col for col in column_names if col != 'id']
                for i, column in enumerate(updateable_columns, start=1):  # A listagem começa em 1
                    print(f"{i}. {column}")
                field_choice = int(input("Escolha: ")) - 1
                new_value = input(f"Digite o novo valor para {updateable_columns[field_choice]}: ")
                setattr(entity, updateable_columns[field_choice], new_value)
                dao.update(entity, id)

            elif action_choice == 3:
                # Excluir registro
                id = int(input("Digite o ID do registro que deseja excluir: "))
                dao.delete(id)

            elif action_choice == 4:
                # Listar todos os registros
                records = dao.get_all()
                for record in records:
                    print(record)

            elif action_choice == 5:
                # Gera um novo exemplo antes de adicionar o registro de exemplo
                current_id = get_last_id(db_path, table) + 1
                generate_example_class(table, column_names, column_types, current_id)
                ExampleClass = import_class(f"examples.{table.capitalize()}Exemplo", f"{table.capitalize()}Exemplo")
                entity = ExampleClass()
                dao.insert(entity)

if __name__ == "__main__":
    main()
