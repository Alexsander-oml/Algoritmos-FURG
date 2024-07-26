# 1. Identificar se a figura é um quadrado ou retângulo
print("1. Identificar se a figura é um quadrado ou retângulo")
largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))

if largura <= 0 or comprimento <= 0:
    print("Erro: Os valores devem ser maiores que zero.")
elif largura == comprimento:
    print("A figura é um quadrado.")
else:
    print("A figura é um retângulo.")

print("\n")

# 2. Verificar condições da viagem
print("2. Verificar condições da viagem")
custo = float(input("Digite o custo da viagem: "))
wifi = input("Terá Wifi? (sim/não): ").strip().lower()
piscina = input("Terá piscina? (sim/não): ").strip().lower()
churrasqueira = input("Terá churrasqueira? (sim/não): ").strip().lower()

if custo >= 30:
    print("A viagem não atende ao requisito de custo.")
elif wifi == "sim" and piscina == "sim":
    print("A viagem está de acordo com todos os requisitos.")
elif wifi == "não" or piscina == "não":
    if churrasqueira == "sim":
        print("A viagem está de acordo com todos os requisitos.")
    else:
        print("A viagem não atende ao requisito de churrasqueira.")
else:
    print("A viagem não atende aos requisitos.")

print("\n")

# 3. Verificar se três medidas podem formar um triângulo e seu tipo
print("3. Verificar se três medidas podem formar um triângulo e seu tipo")
a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Os valores dos lados devem ser positivos.")
elif a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("O triângulo é equilátero.")
    elif a == b or b == c or a == c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os valores fornecidos não podem formar um triângulo.")

print("\n")


''' L1 = int(input('Digite o lado 1 do triãngulo: '))
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

Forma 2:

L1 = int(input('Digite o lado 1 do triângulo: '))
L2 = int(input('Digite o lado 2 do triângulo: '))
L3 = int(input('Digite o lado 3 do triângulo: '))

# Verificando se os lados podem formar um triângulo
if (L2 - L3) < L1 < (L2 + L3) and (L1 - L3) < L2 < (L1 + L3) and (L1 - L2) < L3 < (L1 + L2):
    print('Os lados formam um triângulo.')
else:
    print('Os lados não formam um triângulo.')


Forma 3 Definitiva dizendo qual tipo de triângulo é:

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
'''




# 4. Verificar situação do estudante
print("4. Verificar situação do estudante")
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))
frequencia = float(input("Digite a frequência em porcentagem: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if frequencia < 75:
    print("O estudante está reprovado por frequência.")
elif media < 3:
    print("O estudante rodou sem exame.")
elif media >= 7:
    print("O estudante passou por média.")
else:
    print("O estudante ficou em exame.")

print("\n")

# 5. Verificar se um número é par ou ímpar
print("5. Verificar se um número é par ou ímpar")
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

print("\n")

# 6. Ordenar três números em ordem crescente
print("6. Ordenar três números em ordem crescente")
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

if num1 <= num2 <= num3:
    print(f"Os números em ordem crescente são: {num1}, {num2}, {num3}")
elif num1 <= num3 <= num2:
    print(f"Os números em ordem crescente são: {num1}, {num3}, {num2}")
elif num2 <= num1 <= num3:
    print(f"Os números em ordem crescente são: {num2}, {num1}, {num3}")
elif num2 <= num3 <= num1:
    print(f"Os números em ordem crescente são: {num2}, {num3}, {num1}")
elif num3 <= num1 <= num2:
    print(f"Os números em ordem crescente são: {num3}, {num1}, {num2}")
else:
    print(f"Os números em ordem crescente são: {num3}, {num2}, {num1}")

print("\n")

# 7. Verificar se uma data é válida (desconsiderando anos bissextos)
print("7. Verificar se uma data é válida (desconsiderando anos bissextos)")
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print("Mês inválido.")
elif mes == 2:
    if dia < 1 or dia > 28:
        print("Dia inválido para o mês de fevereiro.")
    else:
        print("A data é válida.")
elif mes in [4, 6, 9, 11]:
    if dia < 1 or dia > 30:
        print("Dia inválido para o mês.")
    else:
        print("A data é válida.")
else:
    if dia < 1 or dia > 31:
        print("Dia inválido para o mês.")
    else:
        print("A data é válida.")

print("\n")

# 8. Campeonato de Futebol
print("8. Campeonato de Futebol")
time1 = input("Digite o nome do 1º time: ")
time2 = input("Digite o nome do 2º time: ")
time3 = input("Digite o nome do 3º time: ")
time4 = input("Digite o nome do 4º time: ")

gols12 = int(input(f"Digite os gols do {time1} x {time2}: "))
gols34 = int(input(f"Digite os gols do {time3} x {time4}: "))

if gols12 > gols12:
    vencedor1 = time1
elif gols12 < gols12:
    vencedor1 = time2
else:
    vencedor1 = input(f"Empate entre {time1} e {time2}. Qual time se classificou? ").strip()

if gols34 > gols34:
    vencedor2 = time3
elif gols34 < gols34:
    vencedor2 = time4
else:
    vencedor2 = input(f"Empate entre {time3} e {time4}. Qual time se classificou? ").strip()

gols_finais1 = int(input(f"Digite os gols do {vencedor1} x {vencedor2}: "))
gols_finais2 = int(input(f"Digite os gols do {vencedor2} x {vencedor2}: "))

if gols_finais1 > gols_finais2:
    print(f"O campeão é {vencedor1}.")
elif gols_finais1 < gols_finais2:
    print(f"O campeão é {vencedor2}.")
else:
    campeao = input(f"Empate na final entre {vencedor1} e {vencedor2}. Qual time é o campeão? ").strip()
    print(f"O campeão é {campeao}.")
