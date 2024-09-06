#1) Leia um String e verifique se é um palindromo Renner = renneR
P = input('Escreva uma palavra e verifique se ela é um PALINDROMO: ')
esp = ''
C = 0
pala = ''

while C < len(P):
    if P[C] != ' ':
        pala = P[C] + pala 
    else:
        esp = esp + pala + ' '  
        pala = '' 
    C += 1

esp = esp + pala

if esp == P:
 print('PALÍNDROMO')
else:
 print('NÃO PALINDROMO')




