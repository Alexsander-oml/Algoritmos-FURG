anoA = int(input('Digite o ano atual: '))
anoN = int(input('Digite o ano que você nasceu: '))
idade = (anoA-anoN)

if idade >= 16 and idade <= 17 or idade >= 70:
 print('Você tem',idade,'anos logo seu voto é facultativo!')
if idade >= 18 and idade < 70:
 print('Você tem',idade,'anos logo pode votar!')
if idade < 16:
 print('Você tem',idade,'anos logo não pode votar!')
 