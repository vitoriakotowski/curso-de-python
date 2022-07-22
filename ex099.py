def maior(* números):
    maior = contador = 0
    for valor in números:
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1 # fez a 2ª leitura indicar o 8 como maior ao invés do 0, não entendi porquê
    tamanho = len(números)
    print(f'Recebi {números}, totalizando {tamanho} números, sendo {maior} o maior.')
    print('.:.' * 30)

maior(2, 1, 7)
maior(8, 0)
maior(4, 4, 7, 6, 2)