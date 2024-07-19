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
     
     '''
     L1 = int(input('Digite o lado 1 do triãngulo: '))
L2 = int(input('Digite o lado 2 do triãngulo: '))
L3 = int(input('Digite o lado 3 do triãngulo: '))
soma1 = L2 + L3
soma2 = L1 + L3
soma3 = L2 + L1

if L1 > soma1 or L2 > soma2 or L3 > soma3:
     '''