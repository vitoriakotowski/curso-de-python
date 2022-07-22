from datetime import date
atual = date.today().year
ano = int(input('Informe o seu ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano + 18))
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    print('Já passaram {} anos do seu alistamento.'.format(idade - 18))
    print('O seu alistamento foi em {}.'.format(ano + 18))