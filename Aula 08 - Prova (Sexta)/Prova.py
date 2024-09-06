'''
1)
Enunciado:
Cada carro tem um desempenho, que é geralmente medido 
por quantos quilômetros ele pode percorrer com 1 litro de gasolina. 
Escreva um programa em Python que leia o desempenho de um carro e um 
trajeto percorrido em um mês. Escreva o quanto foi gasto em reais, considerando a gasolina a R$5,85.

Exemplo fornecido:
Desempenho: 12 km/l
Trajeto: 1000 km
Gasto: R$ 487,50 
'''

D = float(input('Desempenho do carro km/l: '))
T = float(input('Trajeto percorrido em um mês'))
G = 5.85

Gasto = (T/D)*G

print(Gasto)

'''
Questão 2 (3,5 Pontos):

Crie um programa em Python que leia uma data de 2024 ou de 2025 e escreva qual o dia da semana corresponde à data. 
Observe que 2024 é um ano bissexto e que o ano começou em uma segunda-feira.

Exemplo de tabela:

12/01/2024 - Segunda-feira
03/04/2024 - Quarta-feira
31/03/2025 - Segunda-feira
06/04/2025 - Domingo
'''
D = int(input("Informe o dia: "))
M = int(input("Informe o mês: "))
A = int(input("Informe o ano (2024 ou 2025): "))


if A != 2024 and A != 2025:
    print("Ano inválido. Por favor, insira 2024 ou 2025.")
else:
    DP = 0
    if M > 1: DP += 31  # Janeiro
    if M > 2: DP += 28  # Fevereiro (nn precisa do ano bissexto)
    if M > 3: DP += 31  # Março
    if M > 4: DP += 30  # Abril
    if M > 5: DP += 31  # Maio
    if M > 6: DP += 30  # Junho
    if M > 7: DP += 31  # Julho
    if M > 8: DP += 31  # Agosto
    if M > 9: DP += 30  # Setembro
    if M > 10: DP += 31  # Outubro
    if M > 11: DP += 30  # Novembro

    
    DP += D - 1  

    # determina o dia da semana
    DSN = DP % 7

    # mapeia o dia da semana
    if DSN == 0:
        dia_semana = "segunda-feira"
    elif DSN == 1:
        dia_semana = "terça-feira"
    elif DSN == 2:
        dia_semana = "quarta-feira"
    elif DSN == 3:
        dia_semana = "quinta-feira"
    elif DSN == 4:
        dia_semana = "sexta-feira"
    elif DSN == 5:
        dia_semana = "sábado"
    elif DSN == 6:
        dia_semana = "domingo"

    print(f"A data {D:02d}/{M:02d}/{A} é uma {dia_semana}.")


''' 
Questão 3 (3,5 Pontos)

Crie um programa em Python que leia um número inteiro e escreva a soma dos números correspondentes a cada dígito do número. Por exemplo:

Número	Soma
1412	8
4341220	16
101	    2
Nesta questão, você não pode utilizar strings. Deve utilizar operações matemáticas que vimos em aula, como o resto e a divisão inteira.


'''

N = int(input("Digite um número inteiro: "))
soma = 0

while N > 0:
    N2 = N%10
    soma += N2
    N //= 10

print('A soma dos dígitos é: ',soma)


''' 
Questão 4 (1,5 Pontos)

Crie um programa em Python que leia um número inteiro e escreva todos os divisores desse número. Por exemplo:

Número	Divisores
14	1,2,7,14
17	1,17
24	1,2,3,4,6,8,12,24

'''
N = int(input("digite N para ver seus divisores: "))
C = 1

while C <= N:
    if N % C == 0:  
        print(C, end=" ")  
    C += 1  

print()  