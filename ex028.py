from random import randint
from time import sleep
n1 = int(input('Advinhe o número de 0 a 5: '))
sorteado = randint(0, 5) #faz o computador pensar num número entre 0 e 5
print('*-' * 20)
print('PROCESSANDO...')
print('*-' * 20)
sleep(3)
print('O número da vez é:')
print(sorteado)
if n1==sorteado:
    print('Parabéns! Você advinhou!')
else:
    print('Tente novamente.')