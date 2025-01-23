# 12) Implementar um programa para multiplicar matrizes.
# Obs (nro de elementos em cada dimensão):
# 1a matriz = (Linhas1 x Colunas1)
# 2a matriz = (Linhas2 x Colunas2)
# Multiplicação: (Linhas1 x Colunas1) x (Linhas2 x Colunas2), onde Colunas1 = Linhas2
# Resultado: (Linhas1 x Colunas2)
def multiplicar_matrizes(A, B):
    # Obter as dimensões das matrizes
    linhas_A, colunas_A = len(A), len(A[0])
    linhas_B, colunas_B = len(B), len(B[0])

    # Verificar se as matrizes podem ser multiplicadas
    if colunas_A != linhas_B:
        raise ValueError("O número de colunas em A deve ser igual ao número de linhas em B")

    # Inicializar a matriz resultado com zeros
    resultado = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    # Realizar a multiplicação
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado

# Exemplo de uso com função
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

resultado = multiplicar_matrizes(A, B)
for linha in resultado:
    print(linha)

# Exemplo de uso sem função
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Obter as dimensões das matrizes
linhas_A, colunas_A = len(A), len(A[0])
linhas_B, colunas_B = len(B), len(B[0])

# Verificar se as matrizes podem ser multiplicadas
if colunas_A != linhas_B:
    raise ValueError("O número de colunas em A deve ser igual ao número de linhas em B")

# Inicializar a matriz resultado com zeros
resultado = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

# Realizar a multiplicação
for i in range(linhas_A):
    for j in range(colunas_B):
        for k in range(colunas_A):
            resultado[i][j] += A[i][k] * B[k][j]

# Imprimir o resultado
for linha in resultado:
    print(linha)