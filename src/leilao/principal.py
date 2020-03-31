from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

primeiro_usuario = Usuario("Gui")
segundo_usuario = Usuario("Pedro")

lance_do_gui = Lance(primeiro_usuario, 150.00)
lance_do_pedro = Lance(segundo_usuario, 100.00)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_pedro)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()

avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
