lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha][coluna] = int(input(f'Digite um valor para a posição {linha, coluna}: '))
for linha in range(0,3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^6}]', end='')
        if lista[linha][coluna] % 2 == 0:
            pares += lista[linha][coluna]
    print()
print(f'A soma dos números pares digitados totaliza {pares}.')
for linha in range(0, 3):
    terceira += lista[linha][2]
print(f'A soma dos números da 3ª coluna totaliza {terceira}.')
for coluna in range(0, 3):
    if coluna == 0:
        maior = lista[1][coluna]
    elif lista[1][coluna] > maior:
        maior = lista[1][coluna]
print(f'O maior valor da 2ª linha é {maior}.')