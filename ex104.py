def leiaint(a):
    ok = False
    valor = 0
    while True:
        n = input(a)
        if n.isnumeric():
            valor = int(n)
            ok = True
            return valor
        else:
            print('\033[0;31mERRO. Número inválido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')