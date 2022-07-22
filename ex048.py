soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont = cont + 1 #ou cont += c
        soma += c #ou soma = soma + c
print('A soma de todos os {} números ímpares e múltiplos de 3 é igual a {}.'.format(cont, soma))