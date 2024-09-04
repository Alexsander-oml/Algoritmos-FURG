D = int(input("Digite o dia: "))
M = int(input("Digite o mês: "))
A = int(input("Digite o ano: "))
N = int(input("Digite um número de dias: "))

while N > 0:
    if M == 4 or M == 6 or M == 9 or M == 11:
        X = 30
    elif M == 2:
        X = 28
    else:
        X = 31

    D += 1
    N -= 1

    if D > X:
        D = 1
        M += 1

    if M > 12:
        M = 1
        A += 1

print(f"Data final: {D}/{M}/{A}")
