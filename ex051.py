termo = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razão = int(input('Digite a razão desta progressão: '))
dez = termo + (10 - 1) * razão
for c in range(termo, dez + razão, razão):
    print('{}'.format(c), end=' - ')
print('ACABOU!')