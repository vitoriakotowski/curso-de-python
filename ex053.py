frase = str(input('Digite uma frase sem acentos: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('{} é um palíndromo.'.format(frase))
else:
    print('{} não é um palíndromo.'.format(frase))