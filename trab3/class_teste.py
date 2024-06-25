# class_teste.py

import unittest
from datetime import date
from class_funcionario import Funcionario, Assentamento

class TestAssentamentos(unittest.TestCase):

    def setUp(self):
        self.funcionario = Funcionario(matricula=1, nome='João', regime=1, situacao=1, data_nomeacao=date(2023, 1, 1))

    def test_advertencia_verbal_com_afastamento(self):
        afastamento = Assentamento(tipo='Acidente de Trabalho', data_inicio=date(2023, 6, 1), data_fim=date(2023, 6, 15))
        self.funcionario.adicionar_assentamento(afastamento)
        advertencia = Assentamento(tipo='Advertência Verbal', data_inicio=date(2023, 7, 1), data_fim=date(2023, 7, 15))
        self.assertFalse(self.funcionario.adicionar_assentamento(advertencia))

    def test_adiamento_posse_fora_do_prazo(self):
        adiamento = Assentamento(tipo='Adiamento de Posse', data_inicio=date(2023, 2, 1), data_fim=date(2023, 2, 10))
        self.assertFalse(self.funcionario.adicionar_assentamento(adiamento))

    def test_acidente_trabalho_com_afastamento(self):
        afastamento = Assentamento(tipo='Licença Prêmio para Gozo', data_inicio=date(2023, 6, 1), data_fim=date(2023, 6, 30))
        self.funcionario.adicionar_assentamento(afastamento)
        acidente = Assentamento(tipo='Acidente de Trabalho', data_inicio=date(2023, 7, 1), data_fim=date(2023, 7, 15), quantidade_dias=15)
        self.assertFalse(self.funcionario.adicionar_assentamento(acidente))

    def test_falta_justificada_excedente(self):
        falta1 = Assentamento(tipo='Falta Justificada', data_inicio=date(2023, 5, 1), quantidade_dias=3)
        falta2 = Assentamento(tipo='Falta Justificada', data_inicio=date(2023, 6, 1), quantidade_dias=3)
        self.funcionario.adicionar_assentamento(falta1)
        self.assertFalse(self.funcionario.adicionar_assentamento(falta2))

    def test_licenca_premio_validacao(self):
        licenca1 = Assentamento(tipo='Licença Prêmio para Gozo', data_inicio=date(2023, 1, 1), data_fim=date(2023, 1, 30))
        self.assertTrue(self.funcionario.adicionar_assentamento(licenca1))
        licenca2 = Assentamento(tipo='Licença Prêmio para Gozo', data_inicio=date(2023, 2, 1), data_fim=date(2023, 2, 10))
        self.assertFalse(self.funcionario.adicionar_assentamento(licenca2))

    def test_licenca_tratamento_familia_com_afastamento(self):
        afastamento = Assentamento(tipo='Acidente de Trabalho', data_inicio=date(2023, 6, 1), data_fim=date(2023, 6, 15))
        self.funcionario.adicionar_assentamento(afastamento)
        licenca_familia = Assentamento(tipo='Licença Tratamento Família', data_inicio=date(2023, 7, 1), quantidade_dias=30)
        self.assertFalse(self.funcionario.adicionar_assentamento(licenca_familia))

if __name__ == '__main__':
    unittest.main()
