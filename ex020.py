from random import shuffle
a = str(input('Digite o nome dos alunos: 1) '))
b = str(input('2) '))
c = str(input('3) '))
d = str(input('4) '))
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação é: ')
print(lista)