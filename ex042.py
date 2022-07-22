r1 = float(input('Digite o tamanho de uma reta: '))
r2 = float(input('Mais uma: '))
r3 = float(input('A última: '))
if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('Essas retas não formam um triângulo.')
elif r1 == r2 == r3:
    print('Essas retas formam um triângulo equilátero.')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Essas retas formam um triângulo isósceles.')
else:
    print('Essas retas formam um triângulo escaleno.')