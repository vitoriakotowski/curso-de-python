casa = float(input('Qual é o valor da casa? R$'))
salário = float(input('Qual é o seu salário? R$'))
tempo = int(input('Pretende pagar em quantos anos? '))
prestação = casa/(tempo*12)
print('A prestação seria de R${:.2f}.'.format(prestação))
if prestação > salário*0.3:
    print('O seu empréstimo foi negado.')
else:
    print('O seu empréstimo foi aprovado.')