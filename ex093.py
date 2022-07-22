dados = {}
gols = []
print('APROVEITAMENTO DO JOGADOR')
dados['Nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantidade de gols na {c}ª partida: ')))
    dados['Gols'] = gols
    dados['Total'] = sum(gols)
print('.:.' * 30)
print(dados)
print('.:.' * 30)
for k, v in dados.items():
        print(f'{k} tem o valor {v}.')
print('.:.' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f'     {i+1}ª partida - {v} gols.')
print(f'Total de {dados["Total"]} gols.')