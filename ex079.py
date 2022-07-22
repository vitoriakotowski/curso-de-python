continuar = ' '
lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso... ')
    else:
        print('Esse valor já foi digitado, vou ignorar.')
    continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    '''if continuar not in 'Nn':
        break''' # solução do professor, mais curta, mas não contorna respostas erradas
print('-' * 40)
lista.sort()
print(f'Você digitou: {lista}.')
print('-' * 40)