# Monte uma pirâmide dada altura
altura = int(input("Altura: "))
tijolo = input("Tijolo: ")

andar = 1
cont = 1
espaco = " "
desloc = altura - 1


while andar <= altura:
    cont2 = 0
    espaco_montado = ""
    while cont2 < desloc:
        espaco_montado = espaco_montado + espaco
        cont2 = cont2 + 1
    cont2 = 0
    tijolo_montado = ''
    while cont2 < cont:
        tijolo_montado = tijolo_montado + tijolo
        cont2 = cont2 + 1
    print(espaco_montado + tijolo_montado)
    andar = andar + 1
    cont = cont + 2
    desloc = desloc - 1

# Fazer a tabuada de N números
n = int(input("Quantas tabuadas? "))

i = 1
while i <= n:
    j = 0
    print(f"TABUADA DO {i}")
    while j <= 10:
        print(f"{i} * {j} = {i * j}")
        j = j + 1
    i = i + 1
    print()

# Jogo de adivinhação de número
import random

sorteado = random.randint(0, 1_000_000)

num = int(input("Chute um número: "))

while num != sorteado:
    print("Errrouuu!", end=" ")
    if num < sorteado:
        print("O número chutado é menor que o sorteado")
    if num > sorteado:
        print("O número chutado é maior que o sorteado")
    num = int(input("Chute um número: "))

print("Parabéns! Você adivinhou o número!")

# Calcular o fatorial de um número
n = int(input("Digite um número: "))

f = 1
while n > 0:
    f = f * n
    n = n - 1

print(f"O fatorial é: {f}")

# Sequência de Fibonacci até o enésimo termo
n = int(input("Mostrar quantos números? "))

i = 0
fibo = 0
prox = 1
while i < n:
    print(fibo, end=", ")
    soma = fibo + prox
    fibo = prox
    prox = soma
    i = i + 1

# Pirâmide com tijolo e quantidade de andares
tijolo = input("Tijolo: ")
altura = int(input("Número de andares: "))

cont = 1
while cont <= altura:
    andar = altura - cont
    print(" " * andar + tijolo * (2 * cont - 1))
    cont = cont + 1

# Números primos em um intervalo
x = int(input("Início: "))
y = int(input("Fim: "))
while y < x:
    y = int(input("Fim: "))

while x < y:
    c = 1
    p = True
    while c <= x:
        if x == 1:
            p = False
        if not x % c and 1 < c < x:
            p = False
        c = c + 1
    if p:
        print(x, end=", ")
    x = x + 1

# Contagem de 10 minutos
seg = 0
while seg <= 600:
    min = seg // 60
    sec = seg % 60
    print(f"{min:02}:{sec:02}")
    seg = seg + 1

# Funcionários e salários
func = input("Nome do funcionário: ")
sal = float(input(f"Salário de {func}: R$"))

max_sal = sal
max_fun = func

min_sal = sal
min_fun = func

media = sal
count = 1

while func != "fim":
    func = input("Nome do funcionário: ")
    if func != "fim":
        sal = float(input(f"Salário de {func}: R$"))
        if sal > max_sal:
            max_sal = sal
            max_fun = func
        if sal < min_sal:
            min_sal = sal
            min_fun = func
        media = media + sal
        count = count + 1

media = media / count

print(f"O funcionário com maior salário é {max_fun}")
print(f"O funcionário com menor salário é {min_fun}")
print(f"A média dos salários é {media:.2f}")

# Sequência com 2 dígitos, múltiplos de 3 e contendo 1 ou 2
n = 10
while n < 100:
    if not n % 3:
        stmt1 = n % 10 == 1 or n % 10 == 2
        stmt2 = n // 10 == 1 or n // 10 == 2
        if stmt1 or stmt2:
            print(n, end=" ")
    n = n + 1

# Calcular a raiz de um número natural
num = int(input("Digite um número: "))

while num < 0:
    num = int(input("Digite um número: "))

res = 0
raiz = 0
p = 1
while res != num:
    raiz = raiz + p
    res = raiz * raiz
    if res > num:
        if p < 1 / 10000:
            res = num
        raiz = raiz - p
        p = p / 10

print(f"{raiz:.4f}")
