from src.leilao.exception import LanceInvalido

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
            raise LanceInvalido('Valor maior que o valor da carteira.')
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
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def propor_lance(self, lance: Lance):
        if self._lance_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    def _tem_lances(self):
        return self.__lances

    def _lance_valido(self, lance):
        return self._usuario_valido(lance) and self._valor_valido(lance)

    def _usuario_valido(self, lance):
        if not self._tem_lances() or self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('Usuario invalido para propor lance.')

    def _valor_valido(self, lance):
        if not self._tem_lances() or self.__lances[-1].valor < lance.valor:
            return True
        raise LanceInvalido('Valor invalido.')
