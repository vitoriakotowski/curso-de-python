nota1 = float(input('Nota da primeira prova: '))
nota2 = float(input('Nota da segunda prova: '))
média = (nota1 + nota2) / 2
if média > 7:
    print('A sua média é {:.1f}. Status: APROVADO.'.format(média))
elif média < 5:
    print('A sua média é {:.1f}. Status: REPROVADO.'.format(média))
else:
    print('A sua média é {:.1f}. Status: EM RECUPERAÇÃO.'.format(média))