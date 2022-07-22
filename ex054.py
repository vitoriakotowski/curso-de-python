from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = atual - ano
    if idade < 18:
        menor += 1
    else:
        maior +=1
print('{} pessoas são menores de idade.'.format(menor))
print('{} pessoas são maiores de idade.'.format(maior))