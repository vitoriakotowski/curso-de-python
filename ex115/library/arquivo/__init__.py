from ex115.library.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt') # rt means read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # write text e se não existir o + cria
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos;')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # append text
    except:
        print('Erro na abertura do arquivo.')
    else:
        try: # é possível colocar um try dentro de outro
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro na informação dos dados.')
        else:
            print(f'{nome} adicionado com sucesso.')
            a.close()