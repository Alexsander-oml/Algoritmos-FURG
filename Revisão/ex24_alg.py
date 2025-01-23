# 24) Dado o código abaixo, responda:
# str = "Algoritmo e Estrutura de "
# print(str)
# print("1o print - Endereço de str", id(str))
# str += "Dados"
# print(str)
# print("2o print - Endereço de str", id(str))
# Os endereços apresentados na tela são os mesmos? Por que?

# Não, os endereços apresentados na tela não são os mesmos.
# Isso ocorre porque strings em Python são imutáveis.
# Quando você faz uma operação que modifica a string, uma nova string é criada
# e o endereço de memória é diferente.