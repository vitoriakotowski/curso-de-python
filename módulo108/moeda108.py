def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def adicionar(n=0, percentual=0):
    res = n + (n * percentual/100)
    return res


def reduzir(n=0, percentual=0):
    res = n - (n * percentual / 100)
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'. replace('.', ',')