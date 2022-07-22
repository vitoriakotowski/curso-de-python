lista = [[], []]
for contador in range(1, 8):
    número = int(input(f'Digite um valor para a posição {contador}ª: '))
    if número % 2 == 0:
        lista[0].append(número)
    else:
        lista[1].append(número)
lista[0].sort()
lista[1].sort()
print(f'Você digitou os números pares: {lista[0]}.')
print(f'Você digitou os números ímpares: {lista[1]}.')