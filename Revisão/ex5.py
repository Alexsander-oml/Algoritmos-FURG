# 5) Faça uma função em Python para calcular X elevado à Y, ou X
# Y
# . A função deverá receber,
# por parâmetro, X e Y, e retornar o resultado da chamada da subrotina. Exemplo: 2 elevado à
# 3 é igual à 2*2*2 = 8. Os parâmetros são 2 e 3, e o retorno será 8. Obs: implementar
# exatamente como no exemplo, ou seja, a exponenciação deve ser calculada por
# multiplicações sucessivas.

#  for i in range(1, x + 1): # O range vai de 1 até x + 1, pois o range não inclui o último número
#         if x % i == 0:
#             divisores += 1
#     return divisores


def potencia(x, y): #2 e 3
    resultado = 1
    for _ in range(y): # range aqui usamos somente o y, pois o y é o expoente e o _ serve para não usar a variável pq não vamos usar ela
        resultado *= x # resultado = resultado * x porque estamos multiplicando o resultado por x    
    return resultado

def subrotina(x, y):
    aux = ''
    original_y = y
    while y > 0:
        print(y)
        aux += f'*{x}'
        y -= 1
    aux = aux.lstrip('*') + f' = {potencia(x, original_y)}' #lsrtip remove o primeiro caractere da string
    return aux



print(subrotina(2, 3)) # 2*2*2 = 8
print(subrotina(3, 2)) # 3*3 = 9
print(subrotina(4, 4)) # 4*4*4*4 = 256
print(subrotina(5, 5)) # 5*5*5*5*5 = 3125



    