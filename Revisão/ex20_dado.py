import random

# Função que simula o lançamento de um dado
def lancar_dado():
    return random.randint(1, 6)

def main():
    # Lista para armazenar a contagem de cada valor (1-6)
    resultados = [0, 0, 0, 0, 0, 0]
    
    # Lançar o dado 100 vezes
    for _ in range(100):
        resultado = lancar_dado()
        # Incrementar a contagem do valor obtido
        resultados[resultado - 1] += 1 # Os valores vão de 1 a 6, mas a lista começa em 0
    
    # Mostrar quantas vezes cada valor foi conseguido
    for i, resultado in enumerate(resultados): # i é o índice (0-5), resultado é o valor
        print(f"O valor {i + 1} foi conseguido {resultado} vezes.")  # Adicionamos 1 ao índice para mostrar o valor correto

# Executar o programa
main()


# Lista para armazenar a contagem de cada valor (1-6)
resultados = [0, 0, 0, 0, 0, 0]

# Lançar o dado 100 vezes
for _ in range(100):
    resultado = random.randint(1, 6)
    # Incrementar a contagem do valor obtido
    resultados[resultado - 1] += 1  # Os valores vão de 1 a 6, mas a lista começa em 0

# Mostrar quantas vezes cada valor foi conseguido
for i, resultado in enumerate(resultados):  # i é o índice (0-5), resultado é o valor e o enumerate é uma função que retorna o índice e o valor
    print(f"O valor {i + 1} foi conseguido {resultado} vezes.")  # Adicionamos 1 ao índice para mostrar o valor correto
