'''2) Baseado no programa anterior, remova todas as ocorrências do valor zero na lista dos
números positivos. Mostre na tela as três listas, informando a quantidade de zeros que
havia, o total de números remanescentes na lista de positivos e na de negativos.'''

L1 = []
L2 = []
L3 = []
L4 = []
C = 0
C2= 0
Z = 0
N = int(input('Informe quantidade de N: '))
while C < N:
	NA = int(input(f'Informe o número {C + 1}: '))
	L1.append(NA)
	print(f'Lista 1: {L1}')
	C += 1

while C2 < len(L1):
	if L1[C2] >= 0:
		L2.append(L1[C2])
		if L1[C2] >= 0:
			L2.append(L1[C2])
		else:
			L3.append(L1[C2])
			Z = Z + 1
	C2 += 1
	
	


print(f'\nLista 1: {L1} \nLista 2: {L2} \nLista 3: {L3} e o número de Zeros presentes eram: {Z}')