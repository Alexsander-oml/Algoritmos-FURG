"""
def dobro(num):
  saida = num * 2
  return saida

def par_impar(valor):
  if valor % 2 == 0:
     return True
  return False


def test():
    print('Volta às aulas!')
    return 2
    print('Amamos a grama!')


valor = int(input('Digite o número: '))
PI = par_impar(valor)
if PI == True:
   print('Par')
else:
   print('Impar')

num = int(input('Digite o número: '))
duplo = dobro(num)
print(duplo)

"""

'''
def tabuada(num):
    saida = ""
    for i in range(11):
        mult = num * i
        saida = saida + f"{num} x {i} = {mult}\n"
    return saida


for i in range(11):
    print(f"Tabuada do {i}")
    print(tabuada(i))
    print("--------------------------")
'''