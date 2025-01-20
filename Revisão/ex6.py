
"""
Este programa lê duas listas de números, cada uma contendo cinco elementos em ordem crescente.
Em seguida, cria uma terceira lista que é a união das duas primeiras listas, também em ordem crescente.
Finalmente, exibe as três listas e a soma de seus elementos.

Funções utilizadas:
- `sorted()`: Para garantir que as listas estejam em ordem crescente.
- `sum()`: Para calcular a soma dos elementos nas listas.
- `list.extend()`: Para mesclar as duas listas.
"""
# 6) Faça um programa em Python que leia duas listas de números compostas por cinco
# elementos informados de maneira ordenada (números em ordem crescente). Crie uma
# terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a
# soma dos seus elementos contidos.



L1 = []
L2 = []
L3 = []
for _ in range(5):
    aux = int(input("Digite os valores da lista 1: {L1}"))
    L1.append(aux)
    L1.sort()
for _ in range(5):
    aux2 = int(input("Digite os valores da lista 2: {L2}"))
    L2.append(aux2)
    L2.sort()

L3 = (L1 + L2)
L3.sort()
print(L3)

print(f'Lista 1: {L1}')
print(f'Lista 2: {L2}')
print(f'Lista 3: {L3}')

print(f'SOMA DA Lista 1: {sum(L1)}')
print(f'SOMA DA Lista 2: {sum(L2)}')
print(f'SOMA DA Lista 3: {sum(L3)}')
