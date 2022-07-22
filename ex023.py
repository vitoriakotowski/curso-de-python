per = int(input('Digite um número de 0 a 9999: '))
u = per//1%10
d = per//10%10
c = per//100%10
m = per//1000%10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))