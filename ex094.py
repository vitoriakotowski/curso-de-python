dados = {}
lista = []
mulheres = []
soma = média = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('Digite apenas M ou F.')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    if dados['Sexo'] in 'Ff':
        mulheres.append(dados['Nome'])
    lista.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('Digite apenas S ou N.')
    if continuar == 'N':
        break
print(lista)
print(f'{len(lista)} pessoas foram cadastradas.')
média = soma / len(lista)
print(f'A média de idade é de {média:5.2f}.')
print(f'Lista de mulheres: {mulheres}.')
print(f'Pessoas com idade acima da média: ')
for v in range(0, len(lista)):
    if lista[v]['Idade'] > média:
        print(f'Nome: {lista[v]["Nome"]}, Idade: {lista[v]["Idade"]}, Sexo: {lista[v]["Sexo"]}')