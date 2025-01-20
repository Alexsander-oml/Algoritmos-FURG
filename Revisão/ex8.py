# 8) Faça um programa em Python que leia três listas compostas por cinco números fornecidos
# pelo usuário. Crie uma matriz que reúna estas três listas (as listas podem ser as linhas ou as
# colunas da matriz). Apresente o conteúdo da matriz, assim como o seu maior valor contido.

L1 = []
L2 = []
L3 = []
matrix = []

for _ in range(5):
    aux = int(input(f'Digite os valores da lista 1:'))
    L1.append(aux)
    print(f'Lista 1: {L1}')
matrix.append(L1)

for _ in range(5):
    aux = int(input(f'Digite os valores da lista 2:'))
    L2.append(aux)
    print(f'Lista 2: {L2}')
matrix.append(L2)
    
for _ in range(5):
    aux = int(input(f'Digite os valores da lista 3:'))
    L3.append(aux)
    print(f'Lista 3: {L3}')
matrix.append(L3)


print(max([valor for linha in matrix for valor in linha])) # essa linha funciona de forma que ela pega o maior valor de cada linha e depois pega o maior valor de todas as linhas

# a mão
# m = []
# for i in range(4):
#     linha = []
#     for j in range(4):
#         linha.append(int(input()))

#     m.append(linha)

# maior_linha = 0
# maior_coluna = 0
# maior = m[0][0]
# for l in range(4):
#     for c in range(4):        
#         if maior < m[l][c]:
#             maior = m[l][c]
#             maior_linha = l
#             maior_coluna = c

# print('linha do maior: {}\ncoluna do maior: {}'.format(maior_linha, maior_coluna))