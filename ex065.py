soma = contador = média = maior = menor = 0
comando = 'S'
while comando == 'S':
    número = int(input('Digite um número: '))
    soma += número
    contador += 1
    if contador == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
    comando = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
média = (soma) / contador
print('Você digitou {} números e a média entre eles é {}.'.format(contador, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
