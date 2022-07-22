print('Gerador de PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo de uma progressão aritmética: '))
razão = int(input('Digite a razão desta progressão: '))
primeiro = termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} - '.format(primeiro), end='')
        primeiro += razão
        contador +=1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada com {} termos!'.format(total))