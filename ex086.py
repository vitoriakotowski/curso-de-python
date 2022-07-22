lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for contador in range(0, 3):
        lista[linha][contador] = int(input(f'Digite um valor para a posição {linha, contador}: '))
for linha in range(0,3):
    for contador in range(0, 3):
        print(f'[{lista[linha][contador]:^6}]', end='')
    print()