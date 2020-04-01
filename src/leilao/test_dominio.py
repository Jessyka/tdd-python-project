from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def setUp(self):
        self.primeiro_usuario = Usuario("Gui")
        self.segundo_usuario = Usuario("Pedro")
        self.terceiro_usuario = Usuario("Vini")

        self.lance_do_pedro = Lance(self.segundo_usuario, 100.00)
        self.lance_do_gui = Lance(self.primeiro_usuario, 150.00)
        self.lance_do_vini = Lance(self.terceiro_usuario, 80.00)

        self.leilao = Leilao("Celular")


    def test_deve_retornar_maior_e_menor_valor_quando_adicionado_em_ordem_crescente(self):
        self.leilao.propor_lance(self.lance_do_pedro)
        self.leilao.propor_lance(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(150.00, avaliador.maior_lance)

    def test_deve_retornar_maior_e_menor_valor_quando_adicionado_em_ordem_decrescente(self):
        self.leilao.propor_lance(self.lance_do_pedro)
        self.leilao.propor_lance(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(100.00, avaliador.menor_lance)
        self.assertEqual(150.00, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_adicionado_apenas_um_lance(self):
        self.leilao.propor_lance(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150.00, avaliador.menor_lance)
        self.assertEqual(150.00, avaliador.maior_lance)

    def test_deve_retornar_maior_e_menor_valor_quando_tiver_mais_de_dois_lances(self):
        self.leilao.propor_lance(self.lance_do_pedro)
        self.leilao.propor_lance(self.lance_do_gui)
        self.leilao.propor_lance(self.lance_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(80.00, avaliador.menor_lance)
        self.assertEqual(150.00, avaliador.maior_lance)