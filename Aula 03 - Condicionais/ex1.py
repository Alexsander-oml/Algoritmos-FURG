idade = int(input("Digite sua idade: "))
print(idade)

if idade >= 18:
  print("Pode beber cerveja na Lambe!")
  carteira = input('Possui carteira de motorista? ')
  if carteira == 'sim':
    print('Pode dirigir')
  else:
    print('Vá de bus')
else:
    print("Beba leite e ande de bike")

 

'''
if idade < 18:
 print("Não pode ir em open da Lambe!")

if idade >= 18 and idade <= 65:
 print("Pode beber cerveja na Lambe!")

if idade >= 66:
 print("Não deveria nem ir na Lambe")'''