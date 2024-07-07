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
        afastamento = AfastamentoDisciplinar(self.funcionario, "Motivo X", datetime.now(), datetime.now())
        mensagem = afastamento.aplicar()
        self.assertIsNotNone(self.funcionario.licenca_atual)
        print(mensagem)
        self.assertEqual(self.funcionario.licenca_atual.descricao, "Afastamento Disciplinar")

    def test_afastamento_disciplinar_ja_em_licenca(self):
        self.print_test_header("test_afastamento_disciplinar_ja_em_licenca")
        self.funcionario.licenca_atual = "Outra Licença"
        afastamento = AfastamentoDisciplinar(self.funcionario, "Motivo X", datetime.now(), datetime.now())
        try:
            afastamento.aplicar()
        except Exception as e:
            print(e)

    def test_advertencia_verbal(self):
        self.print_test_header("test_advertencia_verbal")
        advertencia = AdvertenciaVerbal(self.funcionario, datetime.now(), datetime.now())
        mensagem = advertencia.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Advertência não coloca o funcionário em licença
        print(mensagem)

    def test_licenca_acompanhamento_conjuge(self):
        self.print_test_header("test_licenca_acompanhamento_conjuge")
        licenca = LicencaAcompanhamentoConjuge(self.funcionario, datetime.now(), datetime.now())
        mensagem = licenca.aplicar()
        self.assertIsNotNone(self.funcionario.licenca_atual)
        print(mensagem)
        self.assertEqual(self.funcionario.licenca_atual.descricao, "Licença Acompanhamento Cônjuge")

    def test_licenca_acompanhamento_conjuge_ja_em_licenca(self):
        self.print_test_header("test_licenca_acompanhamento_conjuge_ja_em_licenca")
        self.funcionario.licenca_atual = "Outra Licença"
        licenca = LicencaAcompanhamentoConjuge(self.funcionario, datetime.now(), datetime.now())
        try:
            licenca.aplicar()
        except Exception as e:
            print(e)

    def test_aposentadoria(self):
        self.print_test_header("test_aposentadoria")
        aposentadoria = Aposentadoria(self.funcionario, datetime.now())
        mensagem = aposentadoria.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Aposentadoria não é uma licença
        print(mensagem)

    def test_falta_justificada(self):
        self.print_test_header("test_falta_justificada")
        falta = FaltaJustificada(self.funcionario, datetime.now(), "Motivo Y")
        mensagem = falta.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Falta justificada não é uma licença
        print(mensagem)

    def test_acidente_trabalho(self):
        self.print_test_header("test_acidente_trabalho")
        acidente = AcidenteTrabalho(self.funcionario, datetime.now(), datetime.now())
        mensagem = acidente.aplicar()
        self.assertIsNotNone(self.funcionario.licenca_atual)
        print(mensagem)
        self.assertEqual(self.funcionario.licenca_atual.descricao, "Acidente de Trabalho")

    def test_acidente_trabalho_ja_em_licenca(self):
        self.print_test_header("test_acidente_trabalho_ja_em_licenca")
        self.funcionario.licenca_atual = "Outra Licença"
        acidente = AcidenteTrabalho(self.funcionario, datetime.now(), datetime.now())
        try:
            acidente.aplicar()
        except Exception as e:
            print(e)

    def test_licenca_premio(self):
        self.print_test_header("test_licenca_premio")
        licenca = LicencaPremio(self.funcionario, 30)
        mensagem = licenca.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Licença prêmio não coloca o funcionário em licença
        print(mensagem)

    def test_licenca_premio_quantidade_dias_invalida(self):
        self.print_test_header("test_licenca_premio_quantidade_dias_invalida")
        licenca = LicencaPremio(self.funcionario, -1)
        with self.assertRaises(Exception):  # Ajuste se usar exceptions personalizadas
            licenca.aplicar()

    def test_exoneracao(self):
        self.print_test_header("test_exoneracao")
        exoneracao = Exoneracao(self.funcionario, datetime.now())
        mensagem = exoneracao.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Exoneração não é uma licença
        print(mensagem)

    def test_exoneracao_ja_em_licenca(self):
        self.print_test_header("test_exoneracao_ja_em_licenca")
        self.funcionario.licenca_atual = "Outra Licença"
        exoneracao = Exoneracao(self.funcionario, datetime.now())
        try:
            exoneracao.aplicar()
        except Exception as e:
            print(e)

    def test_promocao(self):
        self.print_test_header("test_promocao")
        promocao = Promocao(self.funcionario, "Analista", "Analista Sênior", datetime.now())
        mensagem = promocao.aplicar()
        print(mensagem)
        self.assertEqual(self.funcionario.cargo, "Analista Sênior")

    def test_promocao_ja_em_licenca(self):
        self.print_test_header("test_promocao_ja_em_licenca")
        self.funcionario.licenca_atual = "Outra Licença"
        promocao = Promocao(self.funcionario, "Analista", "Analista Sênior", datetime.now())
        try:
            promocao.aplicar()
        except Exception as e:
            print(e)

    def test_treinamento(self):
        self.print_test_header("test_treinamento")
        treinamento = Treinamento(self.funcionario, "Curso X", datetime.now())
        mensagem = treinamento.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Treinamento não é uma licença
        print(mensagem)

    def test_treinamento_sem_nome(self):
        self.print_test_header("test_treinamento_sem_nome")
        treinamento = Treinamento(self.funcionario, "", datetime.now())
        with self.assertRaises(Exception):  # Ajuste se usar exceptions personalizadas
            treinamento.aplicar()

    def test_licenca_saude_molestia_profissional(self):
        self.print_test_header("test_licenca_saude_molestia_profissional")
        licenca = LicencaSaudeMolestiaProfissional(self.funcionario, "Motivo Z", datetime.now(), datetime.now())
        mensagem = licenca.aplicar()
        print(mensagem)
        self.assertIsNotNone(self.funcionario.licenca_atual)
        self.assertEqual(self.funcionario.licenca_atual.descricao, "Licença Saúde Moléstia Profissional")

    def test_licenca_saude_molestia_profissional_datas_invalidas(self):
        self.print_test_header("test_licenca_saude_molestia_profissional_datas_invalidas")
        licenca = LicencaSaudeMolestiaProfissional(self.funcionario, "Motivo Z", datetime.now(), datetime.now() - timedelta(days=1))
        with self.assertRaises(Exception):  # Ajuste se usar exceptions personalizadas
            licenca.aplicar()

    def test_reclusao(self):
        self.print_test_header("test_reclusao")
        reclusao = Reclusao(self.funcionario, datetime.now(), datetime.now())
        mensagem = reclusao.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Reclusão não coloca o funcionário em licença
        print(mensagem)

    def test_reclusao_datas_invalidas(self):
        self.print_test_header("test_reclusao_datas_invalidas")
        reclusao = Reclusao(self.funcionario, datetime.now(), datetime.now() - timedelta(days=1))
        with self.assertRaises(Exception):  # Ajuste se usar exceptions personalizadas
            reclusao.aplicar()

    def test_adiamento_posse(self):
        self.print_test_header("test_adiamento_posse")
        adiamento = AdiamentoPosse(self.funcionario, datetime(2021, 1, 1))
        mensagem = adiamento.aplicar()
        self.assertIsNone(self.funcionario.licenca_atual)  # Adiamento de posse não é uma licença
        print(mensagem)

    def test_adiamento_posse_data_invalida(self):
        self.print_test_header("test_adiamento_posse_data_invalida")
        adiamento = AdiamentoPosse(self.funcionario, datetime(2019, 1, 1))
        with self.assertRaises(Exception) as context:
            adiamento.aplicar()
        print(context.exception)

    def test_licenca_sem_vencimentos(self):
        self.print_test_header("test_licenca_sem_vencimentos")
        licenca = LicencaSemVencimentos(self.funcionario, "Motivo W", datetime.now(), datetime.now())
        mensagem = licenca.aplicar()
        self.assertIsNotNone(self.funcionario.licenca_atual)
        print(mensagem)
        self.assertEqual(self.funcionario.licenca_atual.descricao, "Licença Sem Vencimentos")

    def test_licenca_sem_vencimentos_datas_invalidas(self):
        self.print_test_header("test_licenca_sem_vencimentos_datas_invalidas")
        licenca = LicencaSemVencimentos(self.funcionario, "Motivo W", datetime.now(), datetime.now() - timedelta(days=1))
        with self.assertRaises(Exception) as context:
            licenca.aplicar()
        print(context.exception)

if __name__ == '__main__':
    unittest.main()
