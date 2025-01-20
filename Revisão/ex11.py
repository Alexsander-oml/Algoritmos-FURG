# 11) Implementar um programa para somar matrizes.
# Obs.: as matrizes obrigatoriamente têm a mesma dimensão. Ex.:

def soma_matriz(m1, m2):
    if len(m1) != len(m2):
        raise ValueError("As matrizes devem ter as mesmas dimensões")
    
   
    m3 = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            linha.append(m1[i][j] + m2[i][j])
        m3.append(linha)

    return m3





# Exemplo de uso:
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = soma_matriz(m1, m2)
for linha in resultado:
    print(linha)