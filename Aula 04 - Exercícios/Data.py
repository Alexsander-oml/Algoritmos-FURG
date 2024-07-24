# leia uma data dd, mm, aaaa e diga se ela é válida
# A) Desconsidere ano bissexto
# B) Considere ano bissexto
# ex: 24/07/2024 -> ok


"""sendo quatro (abril 4, junho 6 , setembro 9 e novembro 11) com 30 dias, sete (janeiro 1, março 3, maio 5, julho 7, agosto 8, outubro 10 e dezembro12) com 31 dias e o único mês, fevereiro, com 28 dias (ou 29 dias, nos anos bissextos)
"""

D = int(input("Digite o dia:  "))
M = int(input("Digite o mês: "))
A = int(input("Digite o ano: "))

bissexto = A % 4 == 0 and (A % 100 != 0 or A % 400 == 0)

if M >= 1 and M <= 12:
    if M == 2 and bissexto == True:
        maxD = 29
    if M == 2 and bissexto != True:
        maxD = 28
    if M == 4 or M == 6 or M == 9 or M == 11:
        maxD = 30
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 9 or M == 10 or M == 12:
        maxD = 31

if D >= 1 and D <= maxD:
    print(f"A data {D}/{M}/{A} é valida")
else:
    print(f"A data {D}/{M}/{A} não é valida")

"""
verificar ano bissexto
bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano %400 == 0)
"""
