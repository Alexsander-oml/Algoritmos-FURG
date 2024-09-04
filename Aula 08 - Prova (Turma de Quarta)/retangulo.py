#Tive duas interpretações prisco no dia da prova enviei somente uma mas vou enviar as duas aqui ok :b

#Esse primeiro com verificação somente no IF

L1 = float(input("Digite o comprimento do primeiro lado do retângulo: "))
L2 = float(input("Digite o comprimento do segundo lado do retângulo: "))

if L1 > 0 and L2 > 0:
    A = L1 * L2
    print(f"A área do retângulo é: {A}")
else:
    print("Os lados devem ser números positivos.")

#Esse segundo com verificação com WHILE onde o valor do lado vai ser pedido novamente até ser válido.

L1 = float(input("Digite o comprimento do primeiro lado do retângulo: "))
while L1 <= 0:
    print("O comprimento deve ser um número positivo.")
    L1 = float(input("Digite o comprimento do primeiro lado do retângulo novamente: "))

L2 = float(input("Digite o comprimento do segundo lado do retângulo: "))
while L2 <= 0:
    print("O comprimento deve ser um número positivo.")
    L2 = float(input("Digite o comprimento do segundo lado do retângulo novamente: "))

A = L1 * L2
print(f"A área do retângulo é: {A}")
