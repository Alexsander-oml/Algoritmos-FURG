# ### Exercício 1: União de Listas sem Duplicatas
# Escreva um programa que leia duas listas de números inteiros, cada uma com cinco elementos. O programa deve criar uma terceira lista que contenha a união das duas listas, mas sem números duplicados. Exiba as três listas e a soma dos elementos de cada uma.

lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
lista_uniao = list(set(lista1 + lista2))
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista União:", lista_uniao)
print("Soma Lista 1:", sum(lista1))
print("Soma Lista 2:", sum(lista2))
print("Soma Lista União:", sum(lista_uniao))

# ### Exercício 2: Interseção de Listas
# Escreva um programa que leia duas listas de números inteiros, cada uma com cinco elementos. O programa deve criar uma terceira lista que contenha apenas os números que estão presentes em ambas as listas (interseção). Exiba as três listas e a soma dos elementos de cada uma.

lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
lista_intersecao = list(set(lista1) & set(lista2))
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Interseção:", lista_intersecao)
print("Soma Lista 1:", sum(lista1))
print("Soma Lista 2:", sum(lista2))
print("Soma Lista Interseção:", sum(lista_intersecao))

# ### Exercício 3: Diferença de Listas
# Escreva um programa que leia duas listas de números inteiros, cada uma com cinco elementos. O programa deve criar uma terceira lista que contenha apenas os números que estão presentes na primeira lista, mas não na segunda (diferença). Exiba as três listas e a soma dos elementos de cada uma.

lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
lista_diferenca = list(set(lista1) - set(lista2))
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Diferença:", lista_diferenca)
print("Soma Lista 1:", sum(lista1))
print("Soma Lista 2:", sum(lista2))
print("Soma Lista Diferença:", sum(lista_diferenca))

# ### Exercício 4: Média de Listas
# Escreva um programa que leia duas listas de números inteiros, cada uma com cinco elementos. O programa deve calcular a média dos elementos de cada lista e exibir as médias. Em seguida, crie uma terceira lista que contenha apenas os elementos das duas listas que são maiores que a média das respectivas listas. Exiba as três listas e a soma dos elementos de cada uma.

lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
media1 = sum(lista1) / len(lista1)
media2 = sum(lista2) / len(lista2)
lista_maiores = [x for x in lista1 if x > media1] + [x for x in lista2 if x > media2]
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Maiores que a Média:", lista_maiores)
print("Soma Lista 1:", sum(lista1))
print("Soma Lista 2:", sum(lista2))
print("Soma Lista Maiores que a Média:", sum(lista_maiores))

# ### Exercício 5: Listas Ordenadas
# Escreva um programa que leia duas listas de números inteiros, cada uma com cinco elementos, e ordene cada lista em ordem crescente. Em seguida, crie uma terceira lista que contenha a união das duas listas ordenadas, mas sem números duplicados. Exiba as três listas e a soma dos elementos de cada uma.

lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
lista1.sort()
lista2.sort()
lista_uniao_ordenada = list(set(lista1 + lista2))
lista_uniao_ordenada.sort()
print("Lista 1 Ordenada:", lista1)
print("Lista 2 Ordenada:", lista2)
print("Lista União Ordenada:", lista_uniao_ordenada)
print("Soma Lista 1:", sum(lista1))
print("Soma Lista 2:", sum(lista2))
print("Soma Lista União Ordenada:", sum(lista_uniao_ordenada))

# ### Exercício 6: Listas de Números Pares e Ímpares
# Escreva um programa que leia uma lista de dez números inteiros. O programa deve criar duas listas: uma contendo apenas os números pares e outra contendo apenas os números ímpares. Exiba as três listas e a soma dos elementos de cada uma.

lista = [int(input("Digite um número: ")) for _ in range(10)]
lista_pares = [x for x in lista if x % 2 == 0]
lista_impares = [x for x in lista if x % 2 != 0]
print("Lista Original:", lista)
print("Lista Pares:", lista_pares)
print("Lista Ímpares:", lista_impares)
print("Soma Lista Original:", sum(lista))
print("Soma Lista Pares:", sum(lista_pares))
print("Soma Lista Ímpares:", sum(lista_impares))

# ### Exercício 7: Remover Elementos Específicos
# Escreva um programa que leia uma lista de dez números inteiros e um número inteiro específico. O programa deve criar uma nova lista que contenha todos os elementos da lista original, exceto o número específico informado. Exiba as duas listas e a soma dos elementos de cada uma.

lista = [int(input("Digite um número: ")) for _ in range(10)]
numero_especifico = int(input("Digite o número específico a ser removido: "))
lista_sem_especifico = [x for x in lista if x != numero_especifico]
print("Lista Original:", lista)
print("Lista Sem o Número Específico:", lista_sem_especifico)
print("Soma Lista Original:", sum(lista))
print("Soma Lista Sem o Número Específico:", sum(lista_sem_especifico))

# ### Exercício 8: Contagem de Elementos
# Escreva um programa que leia uma lista de dez números inteiros. O programa deve contar quantas vezes cada número aparece na lista e exibir essa contagem. Em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original. Exiba as duas listas e a soma dos elementos de cada uma.

lista = [int(input("Digite um número: ")) for _ in range(10)]
contagem = {x: lista.count(x) for x in set(lista)}
lista_mais_de_uma_vez = [x for x in contagem if contagem[x] > 1]
print("Lista Original:", lista)
print("Contagem de Elementos:", contagem)
print("Lista com Elementos que Aparecem Mais de Uma Vez:", lista_mais_de_uma_vez)
print("Soma Lista Original:", sum(lista))
print("Soma Lista com Elementos que Aparecem Mais de Uma Vez:", sum(lista_mais_de_uma_vez))



# versoes em forma de funções

# ### Exercício 1: União de Listas sem Duplicatas

def uniao_listas_sem_duplicatas(lista1, lista2):
    lista_uniao = list(set(lista1 + lista2))
    return lista_uniao

def main_exercicio_1():
    lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
    lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
    lista_uniao = uniao_listas_sem_duplicatas(lista1, lista2)
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista União:", lista_uniao)
    print("Soma Lista 1:", sum(lista1))
    print("Soma Lista 2:", sum(lista2))
    print("Soma Lista União:", sum(lista_uniao))

main_exercicio_1()

# ### Exercício 2: Interseção de Listas

def intersecao_listas(lista1, lista2):
    lista_intersecao = list(set(lista1) & set(lista2))
    return lista_intersecao

def main_exercicio_2():
    lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
    lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
    lista_intersecao = intersecao_listas(lista1, lista2)
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista Interseção:", lista_intersecao)
    print("Soma Lista 1:", sum(lista1))
    print("Soma Lista 2:", sum(lista2))
    print("Soma Lista Interseção:", sum(lista_intersecao))

main_exercicio_2()

# ### Exercício 3: Diferença de Listas

def diferenca_listas(lista1, lista2):
    lista_diferenca = list(set(lista1) - set(lista2))
    return lista_diferenca

def main_exercicio_3():
    lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
    lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
    lista_diferenca = diferenca_listas(lista1, lista2)
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista Diferença:", lista_diferenca)
    print("Soma Lista 1:", sum(lista1))
    print("Soma Lista 2:", sum(lista2))
    print("Soma Lista Diferença:", sum(lista_diferenca))

main_exercicio_3()

# ### Exercício 4: Média de Listas

def media_listas(lista1, lista2):
    media1 = sum(lista1) / len(lista1)
    media2 = sum(lista2) / len(lista2)
    lista_maiores = [x for x in lista1 if x > media1] + [x for x in lista2 if x > media2]
    return lista_maiores

def main_exercicio_4():
    lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
    lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
    lista_maiores = media_listas(lista1, lista2)
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista Maiores que a Média:", lista_maiores)
    print("Soma Lista 1:", sum(lista1))
    print("Soma Lista 2:", sum(lista2))
    print("Soma Lista Maiores que a Média:", sum(lista_maiores))

main_exercicio_4()

# ### Exercício 5: Listas Ordenadas

def listas_ordenadas(lista1, lista2):
    lista1.sort()
    lista2.sort()
    lista_uniao_ordenada = list(set(lista1 + lista2))
    lista_uniao_ordenada.sort()
    return lista1, lista2, lista_uniao_ordenada

def main_exercicio_5():
    lista1 = [int(input("Digite um número para a lista 1: ")) for _ in range(5)]
    lista2 = [int(input("Digite um número para a lista 2: ")) for _ in range(5)]
    lista1, lista2, lista_uniao_ordenada = listas_ordenadas(lista1, lista2)
    print("Lista 1 Ordenada:", lista1)
    print("Lista 2 Ordenada:", lista2)
    print("Lista União Ordenada:", lista_uniao_ordenada)
    print("Soma Lista 1:", sum(lista1))
    print("Soma Lista 2:", sum(lista2))
    print("Soma Lista União Ordenada:", sum(lista_uniao_ordenada))

main_exercicio_5()

# ### Exercício 6: Listas de Números Pares e Ímpares

def pares_impares(lista):
    lista_pares = [x for x in lista if x % 2 == 0]
    lista_impares = [x for x in lista if x % 2 != 0]
    return lista_pares, lista_impares

def main_exercicio_6():
    lista = [int(input("Digite um número: ")) for _ in range(10)]
    lista_pares, lista_impares = pares_impares(lista)
    print("Lista Original:", lista)
    print("Lista Pares:", lista_pares)
    print("Lista Ímpares:", lista_impares)
    print("Soma Lista Original:", sum(lista))
    print("Soma Lista Pares:", sum(lista_pares))
    print("Soma Lista Ímpares:", sum(lista_impares))

main_exercicio_6()

# ### Exercício 7: Remover Elementos Específicos

def remover_elemento(lista, numero_especifico):
    lista_sem_especifico = [x for x in lista if x != numero_especifico]
    return lista_sem_especifico

def main_exercicio_7():
    lista = [int(input("Digite um número: ")) for _ in range(10)]
    numero_especifico = int(input("Digite o número específico a ser removido: "))
    lista_sem_especifico = remover_elemento(lista, numero_especifico)
    print("Lista Original:", lista)
    print("Lista Sem o Número Específico:", lista_sem_especifico)
    print("Soma Lista Original:", sum(lista))
    print("Soma Lista Sem o Número Específico:", sum(lista_sem_especifico))

main_exercicio_7()

# ### Exercício 8: Contagem de Elementos

def contagem_elementos(lista):
    contagem = {x: lista.count(x) for x in set(lista)}
    lista_mais_de_uma_vez = [x for x in contagem if contagem[x] > 1]
    return contagem, lista_mais_de_uma_vez

def main_exercicio_8():
    lista = [int(input("Digite um número: ")) for _ in range(10)]
    contagem, lista_mais_de_uma_vez = contagem_elementos(lista)
    print("Lista Original:", lista)
    print("Contagem de Elementos:", contagem)
    print("Lista com Elementos que Aparecem Mais de Uma Vez:", lista_mais_de_uma_vez)
    print("Soma Lista Original:", sum(lista))
    print("Soma Lista com Elementos que Aparecem Mais de Uma Vez:", sum(lista_mais_de_uma_vez))

main_exercicio_8()