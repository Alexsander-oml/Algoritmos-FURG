'''1. Faça um programa que, ao receber os valores da largura e do comprimento de uma figura geométrica, mostre se esta é um quadrado ou apenas um retângulo. Caso um valor seja menor ou igual a zero, deve-se mostrar um erro.
 
 
 
L = float(input("Digite a Largura:  "))
while (L <= 0):
 print('Valor inválido, digite um válido')
 L = float(input("Digite a Largura:  "))
C = float(input("Digite o comprimento: "))
while (C <= 0):
 print('Valor inválido, digite um válido')
 C = float(input("Digite o comprimento: "))
if L == C:
  print(f'A figura é um quadrado\nLargura: {L}\nComprimento{C}')
else:
  print(f'A figura é um retângulo\nLargura: {L}\nComprimento {C}')
 
'''

'''2) Faça um programa em python que pergunte ao usuário o seguinte:

    A viagem custará menos de R$ 30?
    Terá Wifi?
    Terá piscina?
    Terá churrasqueira?

        O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:

    Deverá custar menos de R$ 30
    Tem que ter wifi e piscina
    Se não tiver wifi ou piscina, tem que ter churrasqueira

'''



Valor = input('A viagem custará menos de R$ 30?')
Wifi = input('A viagem terá Wifi?')
Piscina = input('A viagem terá piscina?')
Churras = input('A viagem terá churrasqueira?')
if Valor == 'sim':
  if Wifi == 'sim' or Piscina == 'sim' and Churras == 'sim':
     print('A viagem ocorrerá')
  if Valor != 'sim' and Wifi != 'sim' or Piscina != 'sim' and Churras != 'sim':
    print('A viagem não ocorrerá')
else:
 print('A viagem não ocorrerá')


'''
3) Construa um programa em python que, informadas três medidas a, b e c pelo usuário, verifique se elas podem ser lados de um triângulo. Se não puderem ser, primeiramente o algoritmo deve informar isso. Se for possível serem lados de triângulo, deve dizer qual tipo de triângulo pode ser construído com essas medidas (isósceles, escaleno ou equilátero). A condição para formar um triângulo: comprimento do maior segmento seja inferior à soma dos comprimentos dos dois menores. 
'''

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


'''4) Crie um programa em Python que leia as notas do estudante nos 4 bimestres da nossa disciplina e a frequência (em porcentagem). A seguir informe se o estudante passou por média, rodou ou ficou em exame. Para passar por média, o estudante deve ter média maior ou igual a 7. Estudante com média abaixo de 3 roda sem ao menos fazer o exame. O estudante que tiver menos de 75% de frequência também está rodado na disciplina.'''

N1 = int(input('Digite a nota 1: '))
N2 = int(input('Digite a nota 2: '))
N3 = int(input('Digite a nota 3: '))
N4 = int(input('Digite a nota 4: '))
F = int(input('Frequência em porcentagem: ')
M = (N1 + N2 + N3 + N4/4)
if M >= 7 and F >= 75:
  print('Estudante aprovado!')
if M < 3 or F <= 75:
  print('Estudante reprovado!')
if M >= 3 and M <= 7 or F <= 75:
  print('Estudante reprovado!')  






'''
D = int(input("Digite o dia:  "))
M = int(input("Digite o mês: "))
A = int(input("Digite o ano: "))

bissexto = A % 4 == 0 and (A % 100 != 0 or A % 400 == 0)

if M >= 1 and M <= 12:
    if M == 2 and bissexto == True:
        maxD = 29
    if M == 2 and bissexto != True:
        maxD = 28
    if M == 4 or M == 6 or M == 9 or M == 11:
        maxD = 30
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 9 or M == 10 or M == 12:
        maxD = 31

if D >= 1 and D <= maxD:
    print(f"A data {D}/{M}/{A} é valida")
else:
    print(f"A data {D}/{M}/{A} não é valida")
'''
