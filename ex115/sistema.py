from ex115.library.interface import *
from ex115.library.arquivo import *
from time import sleep

arq = 'cursoemvídeo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # opção de sair do sistema
        cabeçalho('Saindo do sistema... Até mais!')
        break
    else:
        # mensagem de opção errada
        print('\033[31mErro. Digite uma opção válida.\033[m')
    sleep(1)