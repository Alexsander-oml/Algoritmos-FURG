# 18) Faça um programa em Python que receba a temperatura média de cada mês de um
# determinado ano, e armazene-as em uma lista. Em seguida, calcule a média anual das
# temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
# Fevereiro, . . . ).

def ler_temperaturas():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
             "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    temperaturas = []
    for mes in meses:
        temperatura = float(input(f"Digite a temperatura média de {mes}: "))
        temperaturas.append((mes, temperatura))
    return temperaturas

def media_anual(temperaturas):
    return sum(temperatura for mes, temperatura in temperaturas) / len(temperaturas)

def acima_media_anual(temperaturas):
    media = media_anual(temperaturas)
    return [(mes, temperatura) for mes, temperatura in temperaturas if temperatura > media]

def main():
    temperaturas = ler_temperaturas()
    media = media_anual(temperaturas)
    acima_media = acima_media_anual(temperaturas)
    print(f"Média anual: {media}")
    print("Temperaturas acima da média anual:")
    for mes, temperatura in acima_media:
        print(f"{mes} - {temperatura}")

main()

# Versão sem funções

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
            "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

for mes in meses:
    temperatura = float(input(f"Digite a temperatura média de {mes}: "))
    temperaturas.append((mes, temperatura))

media = sum(temperatura for mes, temperatura in temperaturas) / len(temperaturas)
acima_media = [(mes, temperatura) for mes, temperatura in temperaturas if temperatura > media]

print(f"Média anual: {media}")
print("Temperaturas acima da média anual:")
for mes, temperatura in acima_media:
    print(f"{mes} - {temperatura}")

#testes de caso de uso
#caso 1
#input: 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41
#output: Média anual: 35.5
#        Temperaturas acima da média anual:
#        Julho - 36.0
#        Agosto - 37.0
#        Setembro - 38.0
#        Outubro - 39.0
#        Novembro - 40.0

#caso 2
#input: 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
#output: Média anual: 25.5
#        Temperaturas acima da média anual:

#caso 3
#input: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
#output: Média anual: 15.5
#        Temperaturas acima da média anual:
#        Julho - 16.0
#        Agosto - 17.0
#        Setembro - 18.0
#        Outubro - 19.0
#        Novembro - 20.0
#        Dezembro - 21.0
