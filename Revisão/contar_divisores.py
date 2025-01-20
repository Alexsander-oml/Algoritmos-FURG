
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

print(L3)

print(f'Lista 1: {L1}')
print(f'Lista 2: {L2}')
print(f'Lista 3: {L3}')

print(f'SOMA DA Lista 1: {sum(L1)}')
print(f'SOMA DA Lista 2: {sum(L2)}')
print(f'SOMA DA Lista 3: {sum(L3)}')