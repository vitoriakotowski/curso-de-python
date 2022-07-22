s = float(input('Digite o seu salário: '))
if s>1250.00:
    print('Você terá um aumento de 10%, recebendo R${:.2f}.'.format(s*1.1))
else:
    print('O seu aumento será de 15%, totalizando R${:.2f}.'.format(s*1.15))