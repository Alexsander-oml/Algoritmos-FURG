#Leia custo do produto em dólar e escreva o valor em reais

custoD = float(input("Custo do produto em dólar: "))
cotacD = float(input("Cotação do dólar em relação ao real: "))
custoR = custoD*cotacD
print(f"O valor {custoD:.2f}U$ do produto convertido em reais será: {custoR:.2f}R$")
