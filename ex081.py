lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Essa lista tem {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Você digitou, em ordem descrescente: {lista}.')
if 5 in lista:
    print('Achei o número 5.')
else:
    print('Não achei o número 5.')