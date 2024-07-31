#Repetiçao

# Programa 1: Mostra os números de 1 a 10
C = 1
while C <= 10:
    print(C)
    C += 1
print()

# Programa 2: Mostra os números de 10 a 1
C = 10
while C >= 1:
    print(C)
    C -= 1
print()

# Programa 3: Mostra os números pares de 1 a 200
C = 2
while C <= 200:
    print(C)
    C += 2
print()

# Programa 4: Mostra a tabuada (0 a 10) de um número fornecido pelo usuário
N = int(input("Digite um número: "))
C = 0
while C <= 10:
    print(f"{N} x {C} = {N * C}")
    C += 1
print()

# Programa 5: Mostra a sequência de números para um valor N informado pelo usuário
N = int(input("Digite um valor para N: "))
C = 1
while C <= N:
    D = 1
    while D <= C:
        print(C, end=' ')
        D += 1
    print()
    C += 1
print()

# Escadinha

alt = int(input('Altura da escadinha'))
tijolo = input('Do que a escadinha será feita')
C = 1
while C <= alt:
  print(C*tijolo)
  C += 1

# Multiplicando Mario
N = int(input("Digite o número de degraus: "))

cont = 1
while cont <= N:
    print(f"{cont} " * cont)
    cont = cont + 1

# Programa 6: Calcula e mostra a soma dos números de 1 a N
N = int(input("Digite um valor para N: "))
soma = 0
C = 1
while C <= N:
    soma += C
    C += 1
print(f"A soma dos números de 1 a {N} é {soma}")
print()

# Programa 7: Verifica se um número é primo
N = int(input("Digite um número inteiro positivo: "))
if N < 2:
    print(f"{N} não é primo.")
else:
    C = 2
    D = 0
    while C < N:
        if N % C == 0:
            D += 1
        C += 1
    if D == 0:
        print(f"{N} é primo.")
    else:
        print(f"{N} não é primo.")

