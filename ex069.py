contadorm = contadori = contadorh = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    if idade > 18:
        contadori +=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]

    if sexo == 'F' and idade < 20:
        contadorm += 1
    if sexo == 'M':
        contadorh += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{contadori} pessoas tem mais de 18 anos, {contadorh} homens foram cadastrados e {contadorm} mulheres tem menos de 20 anos.')