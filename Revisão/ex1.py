'''1) Faça um programa em Python para ler “n” números inteiros, armazenando-os em uma
lista (o usuário informará um valor inteiro positivo para “n”). Após, crie duas outras listas a
partir desta primeira digitada, sendo que uma conterá os números positivos (>= 0), e a outra
conterá os números negativos. Mostre na tela como ficaram as três listas.
'''
L1 = []
L2 = []
L3 = []
C = 0
C2= 0
N = int(input('Informe quantidade de N: '))
while C < N:
	NA = int(input(f'Informe o número {C + 1}: '))
	L1.append(NA)
	print(f'Lista 1: {L1}')
	C += 1

while C2 < len(L1):
	if L1[C2] >= 0:
		L2.append(L1[C2])
	else:
		L3.append(L1[C2])
	C2 += 1


print(f'\nLista 1: {L1} \nLista 2: {L2} \nLista 3: {L3}')
    

