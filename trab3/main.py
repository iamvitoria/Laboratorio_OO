import unittest
from datetime import datetime, timedelta
from funcionario import Funcionario
from assentamento import *

class TestAssentamentos(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario("João Silva", "12345", "Analista", "TI", datetime(2020, 1, 1))

    def print_test_header(self, test_name):
        print(f"\nRunning test: {test_name}")

    def test_afastamento_disciplinar(self):
        self.print_test_header("test_afastamento_disciplinar")
        afastamento = AfastamentoDisciplinar(self.funcionario, "Comportamento inadequado", datetime(2023, 6, 1), datetime(2023, 6, 30))
        result = afastamento.aplicar()
        self.assertEqual(result, f"Afastamento disciplinar aplicado para João Silva de 2023-06-01 00:00:00 a 2023-06-30 00:00:00. Motivo: Comportamento inadequado")

    def test_advertencia_verbal(self):
        self.print_test_header("test_advertencia_verbal")
        advertencia = AdvertenciaVerbal(self.funcionario, datetime(2023, 5, 1), datetime(2023, 5, 2))
        result = advertencia.aplicar()
        self.assertEqual(result, "Advertência verbal aplicada para João Silva de 2023-05-01 00:00:00 a 2023-05-02 00:00:00.")

    def test_licenca_acompanhamento_conjuge(self):
        self.print_test_header("test_licenca_acompanhamento_conjuge")
        licenca = LicencaAcompanhamentoConjuge(self.funcionario, datetime(2023, 4, 1), datetime(2023, 4, 30))
        result = licenca.aplicar()
        self.assertEqual(result, "Licença para acompanhamento de cônjuge concedida para João Silva de 2023-04-01 00:00:00 a 2023-04-30 00:00:00.")

    def test_aposentadoria(self):
        self.print_test_header("test_aposentadoria")
        aposentadoria = Aposentadoria(self.funcionario, datetime(2023, 7, 1))
        result = aposentadoria.aplicar()
        self.assertEqual(result, "João Silva se aposentou em 2023-07-01 00:00:00")

    def test_falta_justificada(self):
        self.print_test_header("test_falta_justificada")
        falta = FaltaJustificada(self.funcionario, datetime(2023, 3, 1), "Motivo pessoal")
        result = falta.aplicar()
        self.assertEqual(result, "Falta justificada registrada para João Silva em 2023-03-01 00:00:00. Motivo: Motivo pessoal")

    def test_acidente_trabalho(self):
        self.print_test_header("test_acidente_trabalho")
        acidente = AcidenteTrabalho(self.funcionario, datetime(2023, 8, 1), datetime(2023, 8, 15))
        result = acidente.aplicar()
        self.assertEqual(result, "Acidente de trabalho registrado para João Silva de 2023-08-01 00:00:00 a 2023-08-15 00:00:00.")

    def test_licenca_premio(self):
        self.print_test_header("test_licenca_premio")
        licenca = LicencaPremio(self.funcionario, 30)
        result = licenca.aplicar()
        self.assertEqual(result, "Licença prêmio concedida para João Silva por 30 dias")

    def test_exoneracao(self):
        self.print_test_header("test_exoneracao")
        exoneracao = Exoneracao(self.funcionario, datetime(2023, 12, 1))
        result = exoneracao.aplicar()
        self.assertEqual(result, "João Silva foi exonerado em 2023-12-01 00:00:00")

    def test_promocao(self):
        self.print_test_header("test_promocao")
        promocao = Promocao(self.funcionario, "Analista", "Gerente", datetime(2023, 11, 1))
        result = promocao.aplicar()
        self.assertEqual(result, "João Silva foi promovido de Analista para Gerente em 2023-11-01 00:00:00")

    def test_treinamento(self):
        self.print_test_header("test_treinamento")
        treinamento = Treinamento(self.funcionario, "Treinamento de Liderança", datetime(2023, 9, 1))
        result = treinamento.aplicar()
        self.assertEqual(result, "João Silva participou do treinamento 'Treinamento de Liderança' em 2023-09-01 00:00:00")

    def test_licenca_saude_molestia_profissional(self):
        self.print_test_header("test_licenca_saude_molestia_profissional")
        licenca = LicencaSaudeMolestiaProfissional(self.funcionario, "Doença ocupacional", datetime(2023, 10, 1), datetime(2023, 10, 31))
        result = licenca.aplicar()
        self.assertEqual(result, "Licença por saúde/moléstia profissional concedida para João Silva de 2023-10-01 00:00:00 a 2023-10-31 00:00:00. Motivo: Doença ocupacional")

    def test_reclusao(self):
        self.print_test_header("test_reclusao")
        reclusao = Reclusao(self.funcionario, datetime(2023, 2, 1), datetime(2023, 2, 28))
        result = reclusao.aplicar()
        self.assertEqual(result, "João Silva está em reclusão de 2023-02-01 00:00:00 a 2023-02-28 00:00:00")

    def test_adiamento_posse(self):
        self.print_test_header("test_adiamento_posse")
        adiamento = AdiamentoPosse(self.funcionario, datetime(2020, 1, 15))
        result = adiamento.aplicar()
        self.assertEqual(result, "Posse de João Silva adiada para 2020-01-15 00:00:00")

    def test_licenca_sem_vencimentos(self):
        self.print_test_header("test_licenca_sem_vencimentos")
        licenca = LicencaSemVencimentos(self.funcionario, "Estudos", datetime(2023, 1, 1), datetime(2023, 1, 31))
        result = licenca.aplicar()
        self.assertEqual(result, "Licença sem vencimentos concedida para João Silva de 2023-01-01 00:00:00 a 2023-01-31 00:00:00. Motivo: Estudos")

if __name__ == '__main__':
    unittest.main()
