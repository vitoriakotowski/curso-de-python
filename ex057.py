pergunta = str(input('Qual é o seu sexo? M ou F ')).upper()[0].strip()
while pergunta not in 'MmFf':
    pergunta = str(input('Informação inválida. Qual é o seu sexo? M OU F ')).upper()[0]. strip()
print('Sexo {} registrado com sucesso.'.format(pergunta))