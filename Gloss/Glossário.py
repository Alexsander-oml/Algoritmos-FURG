# Tutorial Python: Manipulação de Strings, Listas e Arquivos

# -----------------------------
# Manipulações de Strings
# -----------------------------

print("\n--- Manipulações de Strings ---\n")

# 1. Mudança de Caso
texto = "Hello World"
print("Texto Original:", texto)
print("Maiúsculas:", texto.upper())  # Converte todas as letras para maiúsculas
print("Minúsculas:", texto.lower())  # Converte todas as letras para minúsculas
print("Título:", texto.title())  # Converte o primeiro caractere de cada palavra para maiúscula

# 2. Remoção e Substituição
texto_bagunçado = "   Python é ótimo!   "
print("\nTexto Bagunçado:", texto_bagunçado)
print("Texto Sem Espaços:", texto_bagunçado.strip())  # Remove espaços em branco no início e no fim
print("Texto Substituído:", texto_bagunçado.replace("ótimo", "incrível"))  # Substitui palavras

# 3. Divisão e Junção
frase = "Esta é uma frase de exemplo."
palavras = frase.split()  # Divide uma string em uma lista de palavras
print("\nFrase Dividida em Palavras:", palavras)
frase_junta = "-".join(palavras)  # Junta uma lista de palavras em uma string com "-"
print("Palavras Juntas:", frase_junta)

# 4. Encontrar e Verificar
print("\n'Python' existe no texto?", "Python" in texto_bagunçado)
print("Começa com 'Hello'?", texto.startswith("Hello"))  # Verifica se a string começa com "Hello"
print("Termina com 'World'?", texto.endswith("World"))  # Verifica se a string termina com "World"


# -----------------------------
# Manipulações de Listas
# -----------------------------

print("\n--- Manipulações de Listas ---\n")

# 1. Criação e Acesso
frutas = ["maçã", "banana", "cereja"]
print("Lista Original:", frutas)
print("Primeiro Item:", frutas[0])  # Acessando o primeiro item
print("Último Item:", frutas[-1])  # Acessando o último item

# 2. Modificação
frutas.append("tâmara")  # Adicionando um item ao final
print("\nApós Adicionar:", frutas)
frutas.insert(1, "mirtilo")  # Inserindo um item no índice 1
print("Após Inserir:", frutas)

# 3. Remoção
frutas.remove("banana")  # Remove a primeira ocorrência de "banana"
print("\nApós Remover:", frutas)
item_removido = frutas.pop()  # Remove e retorna o último item
print("Após Remover com Pop:", frutas, ", Item Removido:", item_removido)

# 4. Ordenação e Reversão
numeros = [4, 2, 9, 1, 5]
print("\nNúmeros Originais:", numeros)
numeros.sort()  # Ordena a lista em ordem crescente
print("Números Ordenados:", numeros)
numeros.reverse()  # Inverte a ordem da lista
print("Números Revertidos:", numeros)


# -----------------------------
# Funções Dentro de Colchetes
# -----------------------------

print("\n--- Funções Dentro de Colchetes ---\n")

# 1. Indexação
minha_lista = [10, 20, 30, 40]
print("Lista Original:", minha_lista)
print("Elemento no índice 2:", minha_lista[2])

# 2. Indexação Negativa
print("Último Elemento:", minha_lista[-1])  # Acessa o último elemento

# 3. Fatiamento
print("Fatia do índice 1 ao 3:", minha_lista[1:3])
print("Fatia com passo 2:", minha_lista[::2])
print("Lista Revertida:", minha_lista[::-1])

# 4. Acesso Multidimensional
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matriz)
print("Elemento na linha 2, coluna 3:", matriz[1][2])

# 5. Fatiamento Dinâmico
inicio, fim = 1, 3
print("Fatia Dinâmica:", minha_lista[inicio:fim])


# -----------------------------
# Trabalhando com Matrizes
# -----------------------------

print("\n--- Trabalhando com Matrizes ---\n")

# Criando uma matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:")
for linha in matriz:
    print(linha)

# Acessando elementos
print("\nElemento na linha 2, coluna 3:", matriz[1][2])  # A indexação começa em 0

# Modificando elementos
matriz[0][0] = 10  # Muda o elemento do canto superior esquerdo
print("\nMatriz Modificada:")
for linha in matriz:
    print(linha)

# Adicionando linhas ou colunas
nova_linha = [10, 11, 12]
matriz.append(nova_linha)  # Adiciona uma nova linha
print("\nMatriz após adicionar uma linha:")
for linha in matriz:
    print(linha)

# Iterando pela matriz
print("\nElementos da matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

# Transpondo uma matriz
transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print("\nMatriz Transposta:")
for linha in transposta:
    print(linha)


# -----------------------------
# Manipulações de Arquivos
# -----------------------------

print("\n--- Manipulações de Arquivos ---\n")

# Escrevendo em um arquivo
nome_arquivo = "exemplo.txt"
with open(nome_arquivo, "w") as arquivo:
    arquivo.write("Olá, este é um arquivo de texto de exemplo.\n")
    arquivo.write("Python facilita a manipulação de arquivos!\n")
print(f"Escrito em {nome_arquivo}.")

# Lendo de um arquivo
with open(nome_arquivo, "r") as arquivo:
    print("\nConteúdo do Arquivo:")
    for linha in arquivo:
        print(linha.strip())  # Remove o caractere de nova linha

# Adicionando a um arquivo
with open(nome_arquivo, "a") as arquivo:
    arquivo.write("Adicionando uma nova linha ao arquivo.\n")
print(f"Novo conteúdo adicionado a {nome_arquivo}.")

# Verificando o conteúdo atualizado do arquivo
with open(nome_arquivo, "r") as arquivo:
    print("\nConteúdo Atualizado do Arquivo:")
    print(arquivo.read())