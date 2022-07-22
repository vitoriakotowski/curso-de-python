km = float(input('Você percorreu quantos km? '))
d = int(input('E alugou o carro por quantos dias? '))
p = km*0.15+d*60
print('O valor da locação ficou em R${:.2f}.'.format(p))