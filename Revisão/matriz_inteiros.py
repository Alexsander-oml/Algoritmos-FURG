
# 3) Faça um programa em Python que crie uma matriz de inteiros de cinco linhas por dez
# colunas. Leia os valores desta matriz linha após linha, e exiba a matriz na tela coluna por
# coluna.

# Criar uma matriz
matrix = []
for i in range(5):
    vet = []
    for j in range(10):
        # Lê o valor do usuário para a posição [i][j] da matriz
        valor = int(input(f"Valores de[{i}][{j}]: "))
        vet.append(valor)
    # Adiciona a linha completa na matriz
    matrix.append(vet)

# Exibe a matriz coluna por coluna
for j in range(10):
    for i in range(5):
        # Imprime o valor da posição [i][j] da matriz
        print(matrix[i][j], end=' ')  # o end significa que não vai pular linha após imprimir o valor 
    # Pula para a próxima linha após imprimir todos os valores de uma coluna
    print()