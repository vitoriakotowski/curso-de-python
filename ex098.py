from time import sleep
def contagem(a, b, c):
    for n in range(a, b + 1, c):
        if b <= 0:
            b -= 2
        if c < 0:
            c *= -1
        if c == 0:
            c = 1
        if a > b:
            c *= -1
        print(n, end=' ')
        sleep(0.5)
    print('THE END')
    print('.:.' * 10)


print('CONTAGENS INFINITAS')
print('.:.' * 10)
contagem(1, 10, 1)
contagem(10, 0, -2)
x = int(input('Começo: '))
w = int(input('Fim: '))
y = int(input('Pulo: '))
contagem(x, w, y)

# não tá 100% porque não roda para menos com pulo positivo