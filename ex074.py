from random import randint
número = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
contador = menor = maior = 0
print(f'Eu sorteei os valores: {número}.')
print(f'{max(número)} é o maior número.')
print(f'{min(número)} é o menor número.')