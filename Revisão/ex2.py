'''2) Baseado no programa anterior, remova todas as ocorrências do valor zero na lista dos
números positivos. Mostre na tela as três listas, informando a quantidade de zeros que
havia, o total de números remanescentes na lista de positivos e na de negativos.'''

# Inicializa as listas
L1 = []
L2 = []
L3 = []
C = 0
Z = 0

# Solicita a quantidade de números
N = int(input('Informe quantidade de N: '))

# Preenche a lista L1 com os números informados
while C < N:
	NA = int(input(f'Informe o número {C + 1}: '))
	L1.append(NA)
	print(f'Lista 1: {L1}')
	C += 1

# Separa os números positivos e negativos, e conta os zeros
for num in L1:
	if num > 0:
		L2.append(num)
	elif num < 0:
		L3.append(num)
	else:
		Z += 1

# Remove os zeros da lista de positivos
L2 = [num for num in L2 if num != 0]

# Exibe as listas e as contagens
print(f'\nLista 1: {L1} \nLista 2: {L2} \nLista 3: {L3} e o número de Zeros presentes eram: {Z}')
print(f'Total de números remanescentes na lista de positivos: {len(L2)}')
print(f'Total de números remanescentes na lista de negativos: {len(L3)}')

# Testes de caso:
# Entrada: 5, 1, -1, 0, 2, -2
# Saída esperada:
# Lista 1: [1, -1, 0, 2, -2]
# Lista 2: [1, 2]
# Lista 3: [-1, -2]
# Número de Zeros presentes: 1
# Total de números remanescentes na lista de positivos: 2
# Total de números remanescentes na lista de negativos: 2