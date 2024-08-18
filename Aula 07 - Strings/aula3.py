#Leia um nome e escreva apenas as vogais do nome, diga quantas vogais

N = str(input('Escreva um nome')).lower()
C = 0
CV = 0

while C <= len(N):
    if N[C] == 'a' or N[C] == 'e' or N[C] == 'i' or N[C] == 'o' or N[C] == 'u'
     CV = CV + 1
     print(f'{N[C]}')

print(f'O nome {N} possui {CV} vogais')

N = str(input('Escreva um nome:\n')).lower()  # Converte o nome para minúsculas
C = 0
CV = 0

while C < len(N):  
    if N[C] in 'aeiou':  # Verifica se a letra é uma vogal igual vetor js e afins
        CV += 1
        print(f'{N[C]}')
    C += 1

print(f'O nome {N} possui {CV} vogais')


