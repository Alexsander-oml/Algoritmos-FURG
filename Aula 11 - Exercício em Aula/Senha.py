#Leia uma senha  e diga se ela é 

'''
Forte: 3 tipos
Média: 2 tipos
Fraca: 1 tipo

Numérico
Alfabético
Especial
'''

S = str(input('Digite sua senha e veja se ela é \nForte\nMédia\nFraca: '))

Mai = False
Min = False
Num = False
Esp = False
CS = ''
for C in S:
   V = ord(C)
   if 65 <= V <= 90:
      Mai = True
   elif 97 <= V <= 122:
      Min = True
   elif 48 <= V <= 57:
      Num = True
   else:
      Esp = True
      
if Mai and Min and Num and Esp:
  CS = 'Sua senha é Forte'
elif Mai and Min and Num:
  CS = 'Sua senha é Media'
else:
  CS = 'Sua senha é Fraca'
  
print(CS)
