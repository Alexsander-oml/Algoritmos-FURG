#Decimal pra binário
decimal = int(input("Digite um número decimal: "))

if decimal == 0:
    binario = "0"
else:
    binario = ""
    while decimal > 0:
        binario = str(decimal%2) + binario
        decimal = decimal//2

print(f"O numero binario eh: {binario}")

#Formato função

def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"
    else:
        binario = ""
        while decimal > 0:
            binario = str(decimal%2) + binario
            decimal = decimal//2
        return binario