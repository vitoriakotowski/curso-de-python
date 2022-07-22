print('-'*60)
print('\033[30:46mDescubra a Categoria da Confederação Nacional de Natação\033[m')
print('-'*60)
ano = int(input('Informe o ano de nascimento: '))
from datetime import date
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('{} anos é MIRIM.'.format(idade))
elif idade <= 14:
    print('{} anos é INFANTIL.'.format(idade))
elif idade <=19:
    print('{} anos é JUNIOR.'.format(idade))
elif idade <=25:
    print('{} anos é SÊNIOR.'.format(idade))
else:
    print('{} anos é MASTER.'.format(idade))