lista = []
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input(('Nota 1: '))))
    nota2 = (float(input('Nota 2: ')))
    média = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], média])
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 30)
for índice, aluno in enumerate(lista):
    print(f'{índice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 80)
    opção = int(input('Digite o nome do aluno para ver as suas notas: (999 para sair) '))
    if opção == 999:
        break
    if opção <= len(lista) -1:
        print(f'{lista[opção][0]} tirou as notas {lista[opção][1]}.')