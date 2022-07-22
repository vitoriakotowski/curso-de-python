velocidade = float(input('Qual foi a velocidade detectada? '))
multa = (velocidade-80)*7
if velocidade>80.0:
    print('Você recebeu uma multa de R${:.2f}.'.format(multa))
else:
    print('Parabéns, você estava dentro da velocidade permitida.')