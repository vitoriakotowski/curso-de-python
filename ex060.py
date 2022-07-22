'''from math import factorial
número = int(input('Digite um número para saber o seu fatorial: '))
fatorial = factorial(número)
print('O fatorial de {} é {}.'.format(número, fatorial))'''

número = int(input('Digite um número para saber o seu fatorial: '))
contador = número
fator = 1
print('Calculando {}! '.format(número), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fator = fator * contador
    contador = contador - 1
print('{}.'.format(fator))