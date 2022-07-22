def fatorial(núm, show=False):
    '''Calcula o fatorial de um número
    Núm é o número cujo fatorial será calculado
    Show é um parâmetro opcional para mostrar a conta
    Return: o valor do fatorial de um núm'''

    f = 1
    for c in range(núm, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)