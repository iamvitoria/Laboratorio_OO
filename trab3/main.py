from datetime import date
from funcionario import Funcionario, Assentamento

def main():
    # Criar um funcionário
    funcionario = Funcionario(matricula=1, nome='João', regime=1, situacao=1, data_nomeacao=date(2023, 1, 1))

    # Adicionar alguns assentamentos
    assentamento1 = Assentamento(tipo='Advertência Verbal', data_inicio=date(2023, 3, 1))
    assentamento2 = Assentamento(tipo='Acidente de Trabalho', data_inicio=date(2023, 4, 1), data_fim=date(2023, 4, 10))
    assentamento3 = Assentamento(tipo='Falta Justificada', data_inicio=date(2023, 5, 1), quantidade_dias=2)

    # Tentar adicionar os assentamentos ao funcionário
    if funcionario.adicionar_assentamento(assentamento1):
        print(f"Assentamento '{assentamento1.tipo}' adicionado com sucesso!")
    else:
        print(f"Falha ao adicionar assentamento '{assentamento1.tipo}'.")

    if funcionario.adicionar_assentamento(assentamento2):
        print(f"Assentamento '{assentamento2.tipo}' adicionado com sucesso!")
    else:
        print(f"Falha ao adicionar assentamento '{assentamento2.tipo}'.")

    if funcionario.adicionar_assentamento(assentamento3):
        print(f"Assentamento '{assentamento3.tipo}' adicionado com sucesso!")
    else:
        print(f"Falha ao adicionar assentamento '{assentamento3.tipo}'.")

    # Exibir assentamentos adicionados
    print("Assentamentos do funcionário:")
    for assentamento in funcionario.assentamentos:
        print(f" - Tipo: {assentamento.tipo}, Data Início: {assentamento.data_inicio}")

if __name__ == "__main__":
    main()
