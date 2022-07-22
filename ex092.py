from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('CTPS: [0 se não tiver] '))
if dados['CTPS'] != 0:
    dados['Contrato'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Contrato'] + 35 - nascimento
print('.:.' * 30)
print(dados)
for k, v in dados.items():
        print(f'{k} tem o valor {v}.')