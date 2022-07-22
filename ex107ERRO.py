import moeda108

p = float(input('Digite o preço: R$'))
print(f'A metade de {p:.2f} é {moeda.metade(p):.2f}.')
print(f'O dobro de {p:.2f} é {moeda.dobro(p):.2f}.')
print(f'Adicionando 10%, temos {moeda.adicionar(p, 10):.2f}.')
print(f'Reduzindo 13%, temos {moeda.reduzir(p, 13):.2f}.')