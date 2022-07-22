def área(largura, comprimento):
    print(f'Largura = {largura}m e Comprimento = {comprimento}m.')
    a = largura * comprimento
    print(f'A área do terreno é {a}m².')


# PROGRAMA PRINCIPAL
print('CALCULE A ÁREA DE UM TERRENO')
largura = float(input('Digite a largura do terreno em m: '))
comprimento = float(input('E o comprimento em m: '))
área(largura, comprimento)
print('.:.' * 30)