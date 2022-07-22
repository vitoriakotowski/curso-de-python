from random import randint
vitórias = 0
while True:
    número = int(input('Escolha um número: '))
    sorteado = randint(0,10)
    resultado = número + sorteado
    jogada = ' '
    while jogada not in 'PI':
        jogada = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if resultado % 2 == 0:
        valor = 'PAR'
    else:
        valor = 'ÍMPAR'
    print(f'Você jogou {número} e eu joguei {sorteado}, totalizando {resultado} que é {valor}.')
    if jogada == 'P' and valor == 'PAR':
        print('Você ganhou!')
        vitórias += 1
    elif jogada == 'I' and valor == 'ÍMPAR':
        print('Você ganhou!')
        vitórias += 1
    else:
        print(f'Você teve {vitórias} vitória(s), eu ganhei!')
        break