# 10) Escreva um programa em Python que calcule o comprimento da mais longa sequência de
# espaços em branco em uma string lida.
# Versão com função
def maior_sequencia_espacos(s):
    max_count = 0
    current_count = 0

    for char in s:
        if char == ' ':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count

# Exemplo de uso
string_entrada = input("Digite uma string: ")
print("O comprimento da maior sequência de espaços é:", maior_sequencia_espacos(string_entrada))

# Versão sem função
string_entrada = input("Digite uma string: ")
max_count = 0
current_count = 0

for char in string_entrada:
    if char == ' ':
        current_count += 1
        if current_count > max_count:
            max_count = max_count
    else:
        current_count = 0

print("O comprimento da maior sequência de espaços é:", max_count)