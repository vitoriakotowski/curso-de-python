from random import randint
print('JOKENPÔ')
jogada = int(input('[0] PEDRA, [1] PAPEL OU [2] TESOURA? ' ))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Eu escolhi {} e você escolheu {}!'.format(itens[computador], itens[jogada]))
if jogada == 0:
    if computador == 1:
        print('Ganhei!')
    elif computador == 2:
        print('Você ganhou!')
elif jogada == 1:
    if computador == 0:
        print('Você ganhou!')
    elif computador ==2:
        print('Ganhei!')
elif jogada == 2:
    if computador == 0:
        print('Ganhei!')
    elif computador == 1:
        print('Você ganhou!')
else:
    print('Empatamos. Tente novamente.')