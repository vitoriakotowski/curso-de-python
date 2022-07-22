tupla = (int(input('Valor 1: ')), int(input('Valor 2: ')), int(input('Valor 3: ')), int(input('Valor 4: ')))
contador9 = 0
print(f'Você digitou {tupla}.')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu pela 1ª vez na {tupla.index(3)+1}ª posição.')
else:
    print('O número 3 foi digitado nenhuma vez.')
print(f'Os números pares digitados foram ', end='')
for n in tupla:
    if n % 2 ==0:
        print(f'{n}', end=' ')