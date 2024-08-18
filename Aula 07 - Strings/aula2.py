#Leia um string e escreva letra por letra

P = str(input('Informe uma palavra:\n'))
C = 0

while C <= len(P):
 print(f'{P[C]}')
 C = C + 1