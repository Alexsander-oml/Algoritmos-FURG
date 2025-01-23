# 17) Crie as seguintes listas derivadas da lista informada:
# L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# ● Intervalo de 1 a 9
# ● Intervalo de 8 a 13
# ● Números pares
# ● Números ímpares
# ● Lista reversa

L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Intervalo de 1 a 9
intervalo_1_9 = L[1:10]
print("Intervalo de 1 a 9:", intervalo_1_9)

# Intervalo de 8 a 13
intervalo_8_13 = L[8:14]
print("Intervalo de 8 a 13:", intervalo_8_13)

# Números pares
pares = [num for num in L if num % 2 == 0]
print("Números pares:", pares)

# Números ímpares
impares = [num for num in L if num % 2 != 0]
print("Números ímpares:", impares)

# Lista reversa
reversa = L[::-1]
print("Lista reversa:", reversa)