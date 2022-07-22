def escreva(txt):
    t = len(txt) + 10
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)

texto = str(input('Digite algo: '))
escreva(texto)