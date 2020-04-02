from src.leilao.dominio import Usuario, Leilao
import pytest

@pytest.fixture
def gui():
    return Usuario('gui', 100.00)

def test_deve_subtrair_valor_da_carteira_quando_propor_lance(gui):
    leilao = Leilao('Celular')
    gui.propor_lance(leilao, 50.00)

    assert gui.carteira == 50.00

def test_deve_subtrair_valor_da_carteira_quando_propor_lance_com_mesmo_valor_da_carteira(gui):
    leilao = Leilao('Celular')
    gui.propor_lance(leilao, 100.00)

    assert gui.carteira == 0

def test_deve_lancar_excecao_quando_valor_da_carteira_for_menor_que_lance(gui):
    with pytest.raises(ValueError):
        leilao = Leilao('Celular')

        gui.propor_lance(leilao, 200.00)
