tupla = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
continar = ' '
while True:
    comando = int(input('Digite um número entre 0 e 20: '))
    if comando not in range(0, 21):
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou {tupla[comando]}.')
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        while continuar not in 'SN':
            comando = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        if comando == 'N':
            break
