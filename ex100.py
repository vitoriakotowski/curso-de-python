from random import randint
from time import sleep


def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True) # sem o flush mostra tudo de uma vez
        sleep(0.2)
    print('THE END')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma entre os valores pares sorteados é {soma}.')


números = []
sorteia(números)
somapar(números)