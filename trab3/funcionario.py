from datetime import datetime

class Funcionario:
    def __init__(self, nome, matricula, cargo, departamento, data_admissao):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.departamento = departamento
        self.data_admissao = data_admissao
        self.licenca_atual = None

    def em_outra_licenca(self):
        return self.licenca_atual is not None

    def __str__(self):
        return f"Funcionário: {self.nome} (Matrícula: {self.matricula}, Cargo: {self.cargo}, Departamento: {self.departamento})"
