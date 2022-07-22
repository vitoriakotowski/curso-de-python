distância = float(input('Qual é a distância da sua viagem em KM? '))
if distância<=200:
    print('O valor da sua passagem é R${:.2f}.'.format(distância*0.5))
else:
    print('O valor da sua passagem é R${:.2f}.'.format(distância*0.45))