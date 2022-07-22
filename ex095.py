dados = {}
lista = []
gols = []
print('APROVEITAMENTO DE JOGADORES')
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantidade de gols na {c}ª partida: ')))
        dados['Gols'] = gols
        dados['Total'] = sum(gols)
    lista.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('Digite apenas S ou N.')
    if continuar == 'N':
        break
print('.:.' * 30)
print('Cód.', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    jogador = int(input('Mostrar dados de qual jogados? (999 para sair) '))
    if jogador == 999:
        break
    if jogador >= len(lista):
        print(f'Não existe jogador {jogador}.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {lista[jogador]["Nome"]}')
        for i, gols in enumerate(lista[jogador]['Gols']):
            print(f'No jogo {i+1} fez {gols} gols.')
    print('.:.' * 30)
print('VOLTE SEMPRE')