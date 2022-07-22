soma = contador = 0
while True:
    número = int(input('Digite um número: '))
    if número == 999:
        break
    soma += número
    contador += 1
print(f'{contador} números foram digitados e a soma vale {soma}.')