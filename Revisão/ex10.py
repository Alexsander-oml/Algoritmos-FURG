# 10) Escreva um programa em Python que calcule o comprimento da mais longa sequência de
# espaços em branco em uma string lida.]

# Solicita ao usuário que digite uma string
S = input("Digite a string: ")  # Exemplo de entrada: "Eu   sou alek"

# Inicializa a variável que armazenará o comprimento máximo da sequência de espaços em branco
max = 0

# Inicializa a variável que armazenará o comprimento da sequência atual de espaços em branco
sequencia = 0

# Itera sobre cada caractere na string
for char in S:
    # Verifica se o caractere atual é um espaço em branco
    if char == ' ':
        # Incrementa o comprimento da sequência atual de espaços em branco
        sequencia += 1
        # Atualiza o comprimento máximo se a sequência atual for maior
        if sequencia > max:
            max = sequencia
    else:
        # Reseta a sequência atual se o caractere não for um espaço em branco
        sequencia = 0

# Exibe o comprimento da mais longa sequência de espaços em branco encontrada
print(f'Comprimento da mais longa sequência de espaços em branco: {max}')

              