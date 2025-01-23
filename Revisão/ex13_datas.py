# 13) Faça uma função, em Python, cujo protótipo é QuantosDias(dia, mes, ano),
# que retorne a quantidade de dias do ano até a data informada por parâmetro. Para tanto, é
# preciso verificar o número de dias em cada mês. O mês de fevereiro pode ter 28 ou 29 dias,
# dependendo se o ano for bissexto (verificar).
def QuantosDias(dia, mes, ano):
    def eh_ano_bissexto(ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

    dias_por_mes = [31, 29 if eh_ano_bissexto(ano) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(dias_por_mes[:mes - 1]) + dia

# Versão sem função
ano = 2023
mes = 3
dia = 15
dias_por_mes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_dias = sum(dias_por_mes[:mes - 1]) + dia
print(total_dias)
