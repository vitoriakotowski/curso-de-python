def voto(a):
    from datetime import date # importar a biblioteca/classe apenas para onde será necessária porque isso economiza memória (isso se chama escopo de importação)
    hoje = date.today().year
    idade = hoje - a
    if idade < 16:
        print(f'Você não pode votar com {idade} anos.') # o professor usou return ao invés de print, mas testei e não funcionou
    elif 16 <= idade < 18 or idade > 70:
        print(f'Você tem a opção de votar com {idade} anos.')
    else:
        print(f'Você é obrigado a votar com {idade} anos.')


ano = int(input('Você nasceu em qual ano? '))
voto(ano)