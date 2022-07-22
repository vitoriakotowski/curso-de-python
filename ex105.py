def notas(* n, sit=False):
    '''Função para analisar notas de alunos
    N corresponde às notas
    Sit é um valor opcional que indica a situação do aluno
    Return: dicionário com informações sobre as notas'''
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] < 5:
            print('SITUAÇÃO RUIM.')
        elif r['média'] > 7:
            print('SITUAÇÃO BOA.')
        else:
            print('SITUAÇÃO RAZOÁVEL.')
    return r


resp = notas(5.5, 2.5, 10, sit=True)
print(resp)
help(notas)