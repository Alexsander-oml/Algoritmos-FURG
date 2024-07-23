'''
Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus 
lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
'''  

L1 = int(input('Digite o lado 1 do triãngulo: '))
L2 = int(input('Digite o lado 1 do triãngulo: '))
L3 = int(input('Digite o lado 1 do triãngulo: '))
soma1 = L1 + L2
soma2 = L2 + L3
soma3 = L3 + L1

if L1 > soma1 or L1 > soma2 or L3 < soma3:
    print('triângulo')
    if(L2 > soma1 or L2 > soma2 or L2 < soma3):
        print('triângulo')
        if(L3 > soma1 or L3 > soma2 or L3 < soma3):
            print('triângulo')
        else:
            print('não triângulo')

'''Forma 2:'''

L1 = int(input('Digite o lado 1 do triângulo: '))
L2 = int(input('Digite o lado 2 do triângulo: '))
L3 = int(input('Digite o lado 3 do triângulo: '))

# Verificando se os lados podem formar um triângulo
if (L2 - L3) < L1 < (L2 + L3) and (L1 - L3) < L2 < (L1 + L3) and (L1 - L2) < L3 < (L1 + L2):
    print('Os lados formam um triângulo.')
else:
    print('Os lados não formam um triângulo.')




'''Forma 3 Definitiva dizendo qual tipo de triângulo é:''' 

L1 = int(input('Digite o lado 1 do triângulo: '))
L2 = int(input('Digite o lado 2 do triângulo: '))
L3 = int(input('Digite o lado 3 do triângulo: '))

# verificando lados
if L1 > 0 and L2 > 0 and L3 > 0 and (L2 - L3) < L1 < (L2 + L3) and (L1 - L3) < L2 < (L1 + L3) and (L1 - L2) < L3 < (L1 + L2):
    print('Os lados formam um triângulo.')
    
    # Determinando o tipo de triângulo
    if L1 == L2 == L3:
        print('O triângulo é equilátero.')
    elif L1 == L2 or L1 == L3 or L2 == L3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os lados não formam um triângulo.')




    
