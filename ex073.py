times = ('Corinthians', 'Athletico-PR', 'Palmeiras', 'Atlético-MG', 'Internacional', 'Coritiba', 'Fluminense',
         'América-MG', 'São Paulo', 'Santos', 'BragantinoCeará', 'Botafogo', 'Flamengo', 'Goiás', 'Avaí', 'Cuiabá',
         'Atlético-GO', 'Juventude', 'Fortaleza')
print(f'Os 5 primeiros times são {times[:5]}.')
print(f'Os 4 últimos colocados são {times[-4:]}.')
print(f'Times em ordem alfabética: {sorted(times)}.')
print(f'Botafogo está na posição {times.index("Botafogo")+1}ª.')