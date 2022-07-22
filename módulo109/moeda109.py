def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def adicionar(n=0, percentual=0, formato=False):
    res = n + (n * percentual/100)
    return res if formato is False else moeda(res)


def reduzir(n=0, percentual=0, formato=False):
    res = n - (n * percentual / 100)
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'. replace('.', ',')