senha = input('Digite senha correta: ')
while senha != 'gragas':
 print('Senha incorreta. Tente novamente!')
 senha = input('Digite a senha correta: ')
print('Senha correta')

#Forma com tentativas limitadas

senhaT = input('Digite senha correta: ')
C = 4
while C >= 0:
 if senhaT != 'gragas':
  print(f'Senha incorreta. Tentativas restantes {C}!')
  C-=1
 senha = input('Digite a senha correta: ')
