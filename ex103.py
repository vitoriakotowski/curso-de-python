def ficha(a, b):
    if a == '':
        a = '<desconhecido>'
    if b.isnumeric():
        b = int(b)
    else:
        b = 0
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


nome = str(input('Digite o nome do jogador: ')).strip()
gols = str(input('Digite quantos gols ele fez: ')).strip()
ficha(nome, gols)