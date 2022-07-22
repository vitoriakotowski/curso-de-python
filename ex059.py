from time import sleep
print('Digite dois valores: ')
valor1 = int(input('1) '))
valor2 = int(input('2) '))
operação = 0
while operação != 5:
    operação = int(input('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
    '''))
    if operação == 1:
        print('A soma de {} e {} é {}.'.format(valor1, valor2, valor1 + valor2))
    elif operação == 2:
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
    elif operação == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} o maior valor é {}.'.format(valor1, valor2, maior))
    elif operação == 4:
        print('Informe os valores novamente: ')
        valor1 = int(input('1) '))
        valor2 = int(input('2) '))
    elif operação == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim.')