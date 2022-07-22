somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for pessoa in range(1, 5):
    print('----- {}ª PESSOA ----- '.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
médiaidade = somaidade / 4
print('A média das idades é de {:.2f} anos.'.format(médiaidade))
print('{} é o homem mais velho com {} anos.'.format(nomevelho, maioridadehomem))
print('{} mulheres tem menos de 20 anos de idade.'.format(totalmulher20))