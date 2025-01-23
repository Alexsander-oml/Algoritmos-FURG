# 23) Dado o código abaixo, responda:
# x = 10
# y = 10
# print("x = ", x, "\n")
# print("1o print - Endereço de x", id(x))
# print("2o print - Endereço de y", id(y))
# x -= 1
# print("x = ", x, "\n")
# print(x)
# print("3o print - Endereço de x", id(x))
# a) Os endereços apresentados na tela das variáveis nos 1o e 2o prints são iguais? Por que?
# b) De acordo com a resposta no item (a), qual será o endereço apresentado no 3o print do
# código?

# a) Sim, os endereços apresentados no 1o e 2o prints são iguais porque as variáveis x e y
#    estão referenciando o mesmo objeto imutável (inteiro) com valor 10.

# b) O endereço apresentado no 3o print será diferente dos endereços apresentados no 1o e 2o
#    prints porque, ao modificar o valor de x, um novo objeto imutável (inteiro) é criado com
#    o valor 9, e x passa a referenciar esse novo objeto.