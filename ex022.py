per = str(input('Como é o seu nome completo? ')).strip()
print('Analisando o seu nome...')
print('Em maiúsculas: {}'.format(per.upper()))
print('Em minúsculas: {}'.format(per.lower()))
print('Total de letras: {}'.format(len(per)-per.count(' ')))
#print('Quantas letras tem o primeiro nome: {}'.format(per.find(' ')))
separa = per.split()
print('Quantas letras tem o primeiro nome: {}'.format(len(separa[0])))