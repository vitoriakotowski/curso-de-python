from moeda109 import *

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, True)}.')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}.')
print(f'Adicionando 10%, temos {adicionar(p, 10, True)}.')
print(f'Reduzindo 13%, temos {reduzir(p, 13, True)}.')