#Leia um nome e faça o espelho do nome. 'Alex Santos' -> 'xelA Sotnas'
N = str(input("Informe um nome: "))
esp = ''
C = 0
pala = ''

while C < len(N):
    if N[C] != ' ':
        pala = N[C] + pala 
    else:
        esp = esp + pala + ' '  
        pala = '' 
    C += 1


esp = esp + pala

print(esp)