# 25) Dado o seguinte código:
# def step(x,value):
# x = x + value
# print("2o print - Endereço de x", id(x))
# cont = 0
# print("1o print - Endereço de cont", id(cont))
# while cont < 10:
# step(cont,1)
# print("3o print - Endereço de cont", id(cont))
# print(cont)
# O código executará até o final (últimos prints)? Se não, como tu resolverias alterando o
# mínimo, valendo-se do conhecimento sobre ponteiros em Python?

def step(x, value):
    x = x + value
    print("2o print - Endereço de x", id(x))
    return x

cont = 0
print("1o print - Endereço de cont", id(cont))
while cont < 10:
    cont = step(cont, 1)
print("3o print - Endereço de cont", id(cont))
print(cont)