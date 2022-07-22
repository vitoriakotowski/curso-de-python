from random import randint
from time import sleep
from operator import itemgetter
print('JOGO DE DADOS')
jogadas = {'Jogador A': randint(1, 6),
           'Jogador B': randint(1, 6),
           'Jogador C': randint(1, 6),
           'Jogador D': randint(1, 6),}
ranking = []
print('.' * 35)
for k, v in jogadas.items():
    print(f'{k} tirou {v}.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True) # coloca em ordem conforme os elementos do dicionário na posição 1?
print('.' * 35)
print('RANKING')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} que tirou {v[1]}.')