print('Gerador de PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razão = int(input('Digite a razão desta progressão: '))
primeiro = termo
contador = 1
while contador <= 10:
    print('{} - '.format(primeiro), end='')
    primeiro += razão
    contador +=1
print('ACABOU!')