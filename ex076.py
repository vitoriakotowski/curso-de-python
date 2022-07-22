continuar = ' '
tupla = [] # tupla leia-se lista e lista leia-se tupla
while True:
    lista = (str(input('Produto: ')), int(input('Valor: R$')))
    tupla.append(lista)
    continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)
for posição in tupla:
    print(f'{posição[0]:.<30}', end='')
    print(f'R${posição[1]:>7.2f}')