# class_funcionario.py

from datetime import date

class Funcionario:
    def __init__(self, matricula, nome, regime, situacao, data_nomeacao):
        self.matricula = matricula
        self.nome = nome
        self.regime = regime
        self.situacao = situacao
        self.data_nomeacao = data_nomeacao
        self.assentamentos = []

    def adicionar_assentamento(self, assentamento):
        # Adicione aqui a lógica necessária para verificar as condições e adicionar o assentamento
        self.assentamentos.append(assentamento)
        return True  # ou False, dependendo das condições

class Assentamento:
    def __init__(self, tipo, data_inicio, data_fim=None, quantidade_dias=None):
        self.tipo = tipo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.quantidade_dias = quantidade_dias
