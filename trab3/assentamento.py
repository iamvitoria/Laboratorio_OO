from datetime import datetime

class Funcionario:
    def __init__(self, nome, matricula, cargo, departamento, data_admissao):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.departamento = departamento
        self.data_admissao = data_admissao
        self.licenca_atual = None


class AfastamentoDisciplinar:
    def __init__(self, funcionario, motivo, inicio, fim):
        self.funcionario = funcionario
        self.motivo = motivo
        self.inicio = inicio
        self.fim = fim

    def aplicar(self):
        if self.funcionario.licenca_atual is not None:
            raise Exception("Funcionário já está em outra licença.")
        self.funcionario.licenca_atual = self
        self.descricao = "Afastamento Disciplinar"
        return "Afastamento disciplinar aplicado para {} de {} a {}. Motivo: {}".format(
            self.funcionario.nome, self.inicio, self.fim, self.motivo)


class AdvertenciaVerbal:
    def __init__(self, funcionario, inicio, fim):
        self.funcionario = funcionario
        self.inicio = inicio
        self.fim = fim

    def aplicar(self):
        self.descricao = "Advertência Verbal"
        return "Advertência verbal aplicada para {} de {} a {}.".format(
            self.funcionario.nome, self.inicio, self.fim)


class LicencaAcompanhamentoConjuge:
    def __init__(self, funcionario, inicio, fim):
        self.funcionario = funcionario
        self.inicio = inicio
        self.fim = fim

    def aplicar(self):
        if self.funcionario.licenca_atual is not None:
            raise Exception("Funcionário já está em outra licença.")
        self.funcionario.licenca_atual = self
        self.descricao = "Licença Acompanhamento Cônjuge"
        return "Licença para acompanhamento de cônjuge concedida para {} de {} a {}.".format(
            self.funcionario.nome, self.inicio, self.fim)


class Aposentadoria:
    def __init__(self, funcionario, data):
        self.funcionario = funcionario
        self.data = data

    def aplicar(self):
        self.descricao = "Aposentadoria"
        return "{} se aposentou em {}".format(self.funcionario.nome, self.data)


class FaltaJustificada:
    def __init__(self, funcionario, data, motivo):
        self.funcionario = funcionario
        self.data = data
        self.motivo = motivo

    def aplicar(self):
        self.descricao = "Falta Justificada"
        return "Falta justificada registrada para {} em {}. Motivo: {}".format(
            self.funcionario.nome, self.data, self.motivo)


class AcidenteTrabalho:
    def __init__(self, funcionario, inicio, fim):
        self.funcionario = funcionario
        self.inicio = inicio
        self.fim = fim

    def aplicar(self):
        if self.funcionario.licenca_atual is not None:
            raise Exception("Funcionário já está em outra licença.")
        self.funcionario.licenca_atual = self
        self.descricao = "Acidente de Trabalho"
        return "Acidente de trabalho registrado para {} de {} a {}.".format(
            self.funcionario.nome, self.inicio, self.fim)


class LicencaPremio:
    def __init__(self, funcionario, dias):
        self.funcionario = funcionario
        self.dias = dias

    def aplicar(self):
        if self.dias <= 0:
            raise Exception("Quantidade inválida de dias para a Licença Prêmio.")
        self.descricao = "Licença Prêmio"
        return "Licença prêmio concedida para {} por {} dias".format(
            self.funcionario.nome, self.dias)


class Exoneracao:
    def __init__(self, funcionario, data):
        self.funcionario = funcionario
        self.data = data

    def aplicar(self):
        if self.funcionario.licenca_atual is not None:
            raise Exception("Funcionário já está em outra licença.")
        self.descricao = "Exoneração"
        return "{} foi exonerado em {}".format(self.funcionario.nome, self.data)


class Promocao:
    def __init__(self, funcionario, cargo_atual, novo_cargo, data):
        self.funcionario = funcionario
        self.cargo_atual = cargo_atual
        self.novo_cargo = novo_cargo
        self.data = data

    def aplicar(self):
        if self.funcionario.licenca_atual is not None:
            raise Exception("Funcionário já está em outra licença.")
        self.funcionario.cargo = self.novo_cargo
        self.descricao = "Promoção"
        return "{} foi promovido de {} para {} em {}".format(
            self.funcionario.nome, self.cargo_atual, self.novo_cargo, self.data)


class Treinamento:
    def __init__(self, funcionario, nome, data):
        self.funcionario = funcionario
        self.nome = nome
        self.data = data

    def aplicar(self):
        if not self.nome:
            raise Exception("Nome do treinamento não especificado.")
        self.descricao = "Treinamento"
        return "{} participou do treinamento '{}' em {}".format(
            self.funcionario.nome, self.nome, self.data)


class LicencaSaudeMolestiaProfissional:
    def __init__(self, funcionario, motivo, inicio, fim):
        self.funcionario = funcionario
        self.motivo = motivo
        self.inicio = inicio
        self.fim = fim

    def aplicar(self):
        if self.inicio > self.fim:
            raise Exception("Data de início posterior à data de término para a Licença Saúde Moléstia Profissional.")
        self.funcionario.licenca_atual = self
        self.descricao = "Licença Saúde Moléstia Profissional"
        return "Licença por saúde/moléstia profissional concedida para {} de {} a {}. Motivo: {}".format(
            self.funcionario.nome, self.inicio, self.fim, self.motivo)


class Reclusao:
    def __init__(self, funcionario, inicio, fim):
        self.funcionario = funcionario
        self.inicio = inicio
        self.fim = fim

    def aplicar(self):
        if self.inicio > self.fim:
            raise Exception("Data de início posterior à data de término para a Reclusão.")
        self.descricao = "Reclusão"
        return "{} está em reclusão de {} a {}".format(
            self.funcionario.nome, self.inicio, self.fim)


class AdiamentoPosse:
    def __init__(self, funcionario, data_adiamento):
        self.funcionario = funcionario
        self.data_adiamento = data_adiamento

    def aplicar(self):
        if self.data_adiamento < self.funcionario.data_admissao:
            raise Exception("Data de adiamento anterior à data de nomeação para o Adiamento de Posse.")
        self.descricao = "Adiamento de Posse"
        return "Posse de {} adiada para {}".format(
            self.funcionario.nome, self.data_adiamento)


class LicencaSemVencimentos:
    def __init__(self, funcionario, motivo, inicio, fim):
        self.funcionario = funcionario
        self.motivo = motivo
        self.inicio = inicio
        self.fim = fim

    def aplicar(self):
        if self.inicio > self.fim:
            raise Exception("Data de início posterior à data de término para a Licença Sem Vencimentos.")
        self.funcionario.licenca_atual = self
        self.descricao = "Licença Sem Vencimentos"
        return "Licença sem vencimentos concedida para {} de {} a {}. Motivo: {}".format(
            self.funcionario.nome, self.inicio, self.fim, self.motivo)
