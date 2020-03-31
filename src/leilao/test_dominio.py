from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        primeiro_usuario = Usuario("Gui")
        segundo_usuario = Usuario("Pedro")

        lance_do_gui = Lance(primeiro_usuario, 150.00)
        lance_do_pedro = Lance(segundo_usuario, 100.00)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_pedro)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()

        avaliador.avalia(leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(150.00, avaliador.maior_lance)
