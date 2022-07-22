from random import choice
a = str(input('Nome do aluno: '))
b = str(input('Segundo: '))
c = str(input('Terceiro: '))
d = str(input('Quarto: '))
nomes = [a, b, c, d]
sorteado = choice(nomes)
print('O aluno {} deverá apagar o quadro.'.format(sorteado))