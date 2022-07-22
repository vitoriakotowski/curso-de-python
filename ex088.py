from random import randint
from time import sleep
lista = []
jogo = []
print('JOGOS PARA A MEGA SENA')
quantidade = int(input('Você quer sortear quantos jogos? '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        número = randint(1, 60)
        if número not in lista:
            lista.append(número)
            contador +=1
        if contador >= 5:
            break
    lista.sort()
    jogo.append((lista[:]))
    lista.clear()
    total += 1
print(f'SORTEANDO {quantidade} JOGOS...')
for índice, números in enumerate(jogo):
    print(f'Jogo {índice+1}: {números}')
    sleep(1)
print('BOA SORTE!')