import sys

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propor_lance(self, leilao, valor):
        if self.__carteira < valor:
            raise ValueError('Valor maior que o valor da carteira.')
        leilao.propor_lance(Lance(self, valor))
        self.__carteira -= valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    @property
    def lances(self):
        return self.__lances[:]

    def propor_lance(self, lance: Lance):
        if self._tem_lances() and self._lance_invalido(lance):
            raise ValueError('Esse usuario acabou de propor um lance.')
        else:
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    def _tem_lances(self):
        return self.__lances

    def _lance_invalido(self, lance):
        return self._usuario_invalido(lance) or self._valor_invalido(lance)

    def _usuario_invalido(self, lance):
        return self.__lances[-1].usuario == lance.usuario

    def _valor_invalido(self, lance):
        return self.__lances[-1].valor >= lance.valor
