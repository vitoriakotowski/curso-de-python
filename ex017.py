from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('E do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa é de {:.2f}.'.format(hi))

'''co = float(input('Cateto oposto: '))
ca = float(input('Adjacente: '))
hi = (co**2+ca**2)**(1/2)
print('O comprimento da hipotenusa é {:.2f}.'.format(hi))'''
