informações = {}
informações['Nome'] = str(input('Nome: '))
informações['Média'] = float(input(f'Média de {informações["Nome"]}: '))
if informações['Média'] < 7:
    informações['Situação'] = 'reprovado'
elif 5 <= informações['Média'] < 7:
    informações['Média'] = 'em recuperação'
else:
    informações['Situação'] = 'aprovado'
print('.' * 30)
for k, v in informações.items():
        print(f'{k} é {v}.')