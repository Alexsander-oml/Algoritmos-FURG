# 6) Faça um programa em Python que leia duas listas de números compostas por cinco
# elementos informados de maneira ordenada (números em ordem crescente). Crie uma
# terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a
# soma dos seus elementos contidos.


def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = int(input(f"Digite o {i+1}º número (em ordem crescente): "))
        lista.append(numero)
    return lista

def unir_listas_ordenadas(lista1, lista2):
    return sorted(lista1 + lista2)

def main():
    tamanho = 5
    print("Digite os elementos da primeira lista:")
    lista1 = ler_lista(tamanho)
    
    print("Digite os elementos da segunda lista:")
    lista2 = ler_lista(tamanho)
    
    lista_unida = unir_listas_ordenadas(lista1, lista2)
    
    print("Primeira lista:", lista1)
    print("Segunda lista:", lista2)
    print("Lista unida:", lista_unida)
    print("Soma dos elementos da primeira lista:", sum(lista1))
    print("Soma dos elementos da segunda lista:", sum(lista2))
    print("Soma dos elementos da lista unida:", sum(lista_unida))

main()

#testes de caso de uso
#caso 1
#input: 1, 2, 3, 4, 5
#input: 6, 7, 8, 9, 10
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Versão sem funções

tamanho = 5

print("Digite os elementos da primeira lista:")
lista1 = []
for i in range(tamanho):
    numero = int(input(f"Digite o {i+1}º número (em ordem crescente): "))
    lista1.append(numero)

print("Digite os elementos da segunda lista:")
lista2 = []
for i in range(tamanho):
    numero = int(input(f"Digite o {i+1}º número (em ordem crescente): "))
    lista2.append(numero)

lista_unida = sorted(lista1 + lista2)

print("Primeira lista:", lista1)
print("Segunda lista:", lista2)
print("Lista unida:", lista_unida)
print("Soma dos elementos da primeira lista:", sum(lista1))
print("Soma dos elementos da segunda lista:", sum(lista2))
print("Soma dos elementos da lista unida:", sum(lista_unida))