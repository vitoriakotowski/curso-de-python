from random import randint
from time import sleep
tentativas = 0
n1 = int(input('Advinhe o número de 0 a 10: '))
sorteado = randint(0, 10) #faz o computador pensar num número entre 0 e 9
print('*-' * 20)
print('PROCESSANDO...')
print('*-' * 20)
sleep(1)
print('O número da vez é:')
print(sorteado)
while n1 != sorteado:
    n1 = int(input('Advinhe o número de 0 a 10: '))
    sorteado = randint(0, 10)
    print('*-' * 20)
    print('PROCESSANDO...')
    print('*-' * 20)
    sleep(1)
    print('O número da vez é:')
    print(sorteado)
    tentativas += 1
if n1==sorteado:
    print('Parabéns! Você advinhou, mas precisou de {} tentativas.'.format(tentativas))