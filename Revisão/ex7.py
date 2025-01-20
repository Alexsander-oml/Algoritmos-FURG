# 7) Altere o programa anterior para desprezar os números iguais, caso estes existam.
# Portanto, a lista final não deve possuir números iguais armazenados.

L1 = []
L2 = []
L3 = []
for _ in range(5):
    aux = int(input("Digite os valores da lista 1: "))
    L1.append(aux)
    L1.sort()
for _ in range(5):
    aux2 = int(input("Digite os valores da lista 2: "))
    L2.append(aux2)
    L2.sort()

L3 = list(set(L1 + L2))
L3.sort()

# def remove_repetidos(lista):
#     l = []
#     for i in lista:
#         if i not in l:
#             l.append(i)
#     l.sort()
#     return l

# lista = [1, 1, 2, 1, 3, 4,             3, 6, 7, 6, 7, 8, 10 ,9]

# lista = remove_repetidos(lista)
# print (lista)

print(L3)

# print(f'Lista 1: {L1}')
# print(f'Lista 2: {L2}')
# print(f'Lista 3: {L3}')

# print(f'SOMA DA Lista 1: {sum(L1)}')
# print(f'SOMA DA Lista 2: {sum(L2)}')
# print(f'SOMA DA Lista 3: {sum(L3)}')
