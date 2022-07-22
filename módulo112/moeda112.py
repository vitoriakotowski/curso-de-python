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


def resumo(n=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Metade: \t\t\t{metade(n, True)}')
    print(f'Dobro: \t\t\t\t{dobro(n, True)}')
    print(f'Adição de {taxaa}%: \t\t{adicionar(n, taxaa, True)}')
    print(f'Redução de {taxar}%: \t\t{reduzir(n, taxar, True)}')
    print('-' * 30)


def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: {entrada} não é um preço.\033[m')
        else:
            válido = True
            return float(entrada)