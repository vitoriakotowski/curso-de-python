print('{:=^40}'.format('LOJAS LELIS'))
preço = float(input('Preço: R$ '))
condição = int(input('''Forma de pagamento:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 3x no cartão
[4] 3x ou mais no cartão
'''))
if condição == 1:
    print('Com 10% de desconto você paga R${:.2f}.'.format(preço * 0.9))
elif condição == 2:
    print('Com 5% de desconto, você paga R${:.2f}.'.format(preço * 0.95))
elif condição == 3:
    print('Você paga o preço normal de R${:.2f}, sendo a parcela de R${:.2f}.'.format(preço, preço/3))
elif condição == 4:
    parcela = int(input('Em quantas parcelas? '))
    print('Com 20% de juros, você paga parcelas de R${:.2f}, totalizando R${:.2f}.'.format((preço * 1.2) / parcela, preço * 1.2))
else:
    print('Condição inválida. Tente novamente.')