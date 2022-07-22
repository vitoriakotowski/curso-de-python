lista = []
for contador in range(0, 5):
    valor = (int(input(f'Digite um valor: ')))
    '''if contador == 0:
        lista.append(valor)
    elif valor > lista[-1]: # se o valor for maior do que o último valor da lista
        lista.append(valor)'''
    if contador == 0 or valor > lista[-1]: # versão simplificada das últimas 4 litras
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista): # vai da posição 0 até a última
            if valor <= lista[posição]: # verifica em cada posição se o valor que eu quero inserir é = ou <
                lista.insert(posição, valor) # se ele for < ou =, vou inserir ele numa posição específica
                print(f'Adicionado na posição {posição} da lista...')
                break
            posição += 1 # para passar para a próxima posição
print('-' * 50)
print(f'Os valores digitados em ordem são: {lista}.')
print('-' * 50)