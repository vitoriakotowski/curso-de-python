frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A letra A aparece pela 1ª vez na posição {}.'.format(frase.find('A')+1))
print('E pela última vez na posição {}.'.format(frase.rfind('A')+1))