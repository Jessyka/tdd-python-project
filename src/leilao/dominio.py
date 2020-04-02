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
        if self.__lances and (self.__lances[-1].usuario == lance.usuario or self.__lances[-1].valor >= lance.valor):
            raise ValueError('Esse usuario acabou de propor um lance.')
        else:
            self.__lances.append(lance)
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
