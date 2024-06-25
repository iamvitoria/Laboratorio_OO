import unittest
from datetime import date

# Implementação das classes Funcionario e Assentamento
class Funcionario:
    def __init__(self, matricula, nome, regime, situacao, data_nomeacao):
        self.matricula = matricula
        self.nome = nome
        self.regime = regime
        self.situacao = situacao
        self.data_nomeacao = data_nomeacao
        self.assentamentos = []

    def adicionar_assentamento(self, assentamento):
        if self.validar_assentamento(assentamento):
            self.assentamentos.append(assentamento)
            return True
        return False

    def validar_assentamento(self, assentamento):
        if assentamento.tipo == 'Advertência Verbal' and self.tem_afastamento():
            return False
        if assentamento.tipo == 'Adiamento de Posse' and not self.validar_adiamento_posse(assentamento):
            return False
        if assentamento.tipo == 'Acidente de Trabalho' and (self.tem_afastamento() or self.tem_licenca_premio()):
            return False
        if assentamento.tipo == 'Falta Justificada' and not self.validar_falta_justificada(assentamento):
            return False
        if assentamento.tipo == 'Licença Prêmio para Gozo' and not self.validar_licenca_premio(assentamento):
            return False
        if assentamento.tipo == 'Licença Tratamento Família' and self.tem_afastamento():
            return False
        if assentamento.tipo == 'Licença Tratamento Saúde' and self.tem_afastamento():
            return False
        if assentamento.tipo == 'Licença Tratar Interesse Pessoal' and (self.em_estagio_probatorio() or self.tem_afastamento()):
            return False
        if assentamento.tipo == 'LTSI' and self.tem_afastamento():
            return False
        if assentamento.tipo == 'Repreende Servidor' and self.tem_afastamento():
            return False
        return True

    def tem_afastamento(self):
        for assentamento in self.assentamentos:
            if assentamento.tipo in ['Acidente de Trabalho', 'Licença Prêmio para Gozo', 'Licença Tratamento Saúde']:
                return True
        return False

    def tem_licenca_premio(self):
        for assentamento in self.assentamentos:
            if assentamento.tipo == 'Licença Prêmio para Gozo':
                return True
        return False

    def em_estagio_probatorio(self):
        return False

    def validar_adiamento_posse(self, assentamento):
        if (assentamento.data_inicio - self.data_nomeacao).days > 15:
            return False
        return True

    def validar_falta_justificada(self, assentamento):
        if self.regime != 1 or self.situacao == 4:
            return False
        total_dias = sum(a.quantidade_dias for a in self.assentamentos if a.tipo == 'Falta Justificada')
        if total_dias + assentamento.quantidade_dias > 5:
            return False
        return True

    def validar_licenca_premio(self, assentamento):
        return True

class Assentamento:
    def __init__(self, tipo, data_inicio, data_fim=None, quantidade_dias=None):
        self.tipo = tipo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.quantidade_dias = quantidade_dias

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
    unittest.main(exit=False)  # Executar testes unitários e permitir que a execução do main continue
