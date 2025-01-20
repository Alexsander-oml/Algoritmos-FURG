# Faça uma função em Python que receba, por parâmetro, um número inteiro x > 0, e
# retorne o número de divisores positivos que x tem. Por exemplo: o número 12 tem 6
# divisores (1, 2, 3, 4, 6 e 12).

def contar_divisores(x):
    if x <= 0:
        return("O número deve ser maior que 0")
    divisores = 0
    for i in range(1, x + 1): # O range vai de 1 até x + 1, pois o range não inclui o último número
        if x % i == 0:
            divisores += 1
    return divisores

print(contar_divisores(12))