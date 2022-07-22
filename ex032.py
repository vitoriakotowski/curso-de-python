from datetime import date
ano = int(input('Descubra se um ano é bissexto (coloque 0 para o ano atual): '))
if ano==0:
    ano=date.today().year
if ano%4 == 0 and ano%100!=0 or ano%400==0:
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto.')