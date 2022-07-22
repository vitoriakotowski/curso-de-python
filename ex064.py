número = contador = soma = 0
número = int(input('Digite um número inteiro ou 999 para sair: '))
while número != 999:
    contador = contador + 1
    soma = soma + número
    número = int(input('Digite um número inteiro ou 999 para sair: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(contador, soma))
