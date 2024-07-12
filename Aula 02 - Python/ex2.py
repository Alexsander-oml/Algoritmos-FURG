#leia a distancia percorrida e o tempo gasto escreva a velocidade
#O int converte string em números inteiros
#O float converte string em números reais 
#Pula linhas pra organizar
#Pode nao rodar se deixar espaços vagos

Dist = int(input('Distância percorrida '))
Temp = int(input('Tempo Gasto '))
velo = Dist/Temp
print(f'Sua velocidade é {velo:.2f}')
print("A velocidade é: ",velocidade)
print("A velocidade é: " + str(velo))

#print("A velocidade é: " + velo) = erro de concatenate str (not "float") to str.