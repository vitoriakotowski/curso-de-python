print('\033[30:43mCalcule o seu IMC\033[m')
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / altura ** 2
print('Você tem {:.1f} de IMC '.format(imc), end="")
if imc < 18.5:
    print('e está abaixo do peso.')
elif imc <25:
    print('e está com o peso ideal.')
elif imc < 30:
    print('e está com sobrepeso.')
elif imc < 40:
    print('e está com obesidade.')
else:
    print('e está com obesidade mórbida.')