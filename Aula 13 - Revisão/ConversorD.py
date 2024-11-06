#Binário pra Decimal
'''
binario = input("Digite um número Binario: ")

dec = 0
potencia = 1

for digito in binario[::-1]:
   dec += int(digito) * potencia
   potencia *= 2
print("o numero em decimal é: ", dec) 
'''
#Formato função

def binario_para_decimal(binario):
    dec = 0
    potencia = 1

    for digito in binario[::-1]:
        dec += int(digito) * potencia
        potencia *= 2
    return dec

#Teste da função
print(binario_para_decimal("101")) #5