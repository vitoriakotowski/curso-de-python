lista = []
par = []
ímpar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        ímpar.append(valor)
    continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Você digitou os números: {lista}.')
print(f'{par} são pares.')
print(f'{ímpar} são ímpares.')