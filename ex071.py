print('=' * 30)
print('{:^30}'.format('BANCO VLKC'))
print('=' * 30)
saque = int(input('Quanto você quer sacar? R$'))
total = saque
cédula = 50
totalc = 0
while True:
    if total >= cédula:
        total -= cédula
        totalc += 1
    else:
        if totalc > 0:
            print(f'Total de {totalc} cédula(s) de R${cédula:.2f}.')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalc = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre!')