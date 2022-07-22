def adicionar(n=0, percentual=0):
    res = n + (n * percentual/100)
    return res


def reduzir(n=0, percentual=0):
    res = n - (n * percentual / 100)
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'. replace('.', ',')


def resumo(n=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Metade: \t\t\t{moeda(metade(n))}')
    print(f'Dobro: \t\t\t\t{moeda(dobro(n))}')
    print(f'Adição de {taxaa}%: \t\t{moeda(adicionar(n, taxaa))}')
    print(f'Redução de {taxar}%: \t{moeda(reduzir(n, taxar))}')
    print('-' * 30)