total = mil = menor = contador = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    contador += 1
    total +=preço
    if preço > 1000:
        mil += 1
    if contador == 1 or preço < menor:
            menor = preço
            menor = nome
    comando = ' '
    while comando not in 'SN':
        comando = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if comando == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total da compra: R${total:.2f}.')
print(f'{mil} produtos custaram mais de R$1.000,00.')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}.')