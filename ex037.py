número = int(input('Digite um número inteiro: '))
print('Escolha qual será a base de conversão: ')
base = int(input('''[ 1 ] para binário,
[ 2 ] para octal e
[ 3 ] para hexadecimal: '''))
if base==1:
    print('{} convertido para binário é {}.'.format(número, bin(número)[2:]))
elif base==2:
    print('{} convertido para octal é {}.'.format(número, oct(número)[2:]))
elif base==3:
    print('{} convertido para hexadecimal é {}.'.format(número, hex(número)[2:]))
else:
    print('Base inválida, tente novamente.')
