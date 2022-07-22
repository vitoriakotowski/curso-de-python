expressão = str(input('Digite uma expressão: '))
abreparênteses = fechaparêntese = 0
for símbolo in expressão:
    if símbolo == '(':
        abreparênteses += 1
    if símbolo == ')':
        fechaparêntese += 1
if abreparênteses == fechaparêntese:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
# a solução do professor foi diferente, esta está errada porque valida expressão )a+b(