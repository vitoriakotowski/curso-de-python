temporário = []
lista = []
maior = menor = 0
while True:
    temporário.append(str(input('Nome: ')))
    temporário.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temporário[1]
    else:
        if temporário[1] > maior:
            maior = temporário[1]
        if temporário[1] < menor:
            menor = temporário[1]
    lista.append(temporário[:])
    temporário.clear()
    continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'{maior}kg foi o maior peso, sendo de ', end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end=' ')
print()
print(f'{menor}kg foi o menor peso, sendo de ', end='')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end=' ')