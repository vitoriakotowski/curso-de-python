lista = []
for contador in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {contador}: ')))
print(f'Você digitou {lista}.')
print(f'{max(lista)} é o maior número e está na posição ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
print(f'{min(lista)} é o menor número e está na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')