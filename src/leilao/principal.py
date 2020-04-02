from src import Usuario, Lance, Leilao

primeiro_usuario = Usuario("Gui")
segundo_usuario = Usuario("Pedro")

lance_do_gui = Lance(primeiro_usuario, 150.00)
lance_do_pedro = Lance(segundo_usuario, 100.00)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_pedro)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

print(f'O menor lance foi de {lance.menor_lance} e o maior lance foi de {lance.maior_lance}')
