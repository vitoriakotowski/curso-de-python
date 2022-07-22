from moeda108 import *

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}.')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}.')
print(f'Adicionando 10%, temos {moeda(adicionar(p, 10))}.')
print(f'Reduzindo 13%, temos {moeda(reduzir(p, 13))}.')

# já simplificado