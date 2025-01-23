# Crie um programa que leia um arquivo texto e conte o número de linhas. 
# Escreva o número de linhas em um arquivo de saída.

def contar_linhas(arquivo_entrada, arquivo_saida): # Crie uma função que receba o nome de um arquivo de entrada e
    try: # de um arquivo de saída. O arquivo de entrada contém um texto com várias linhas.
        with open(arquivo_entrada, 'r') as entrada: # O programa deve contar o número de linhas do texto e escrever esse número no arquivo de saída.
            linhas = entrada.readlines() # Caso o arquivo de entrada não exista, o programa deve exibir uma mensagem de erro.
            numero_linhas = len(linhas) # O arquivo de saída deve conter a mensagem "Número de linhas: X", onde X é o número de linhas do arquivo de entrada.
        
        with open(arquivo_saida, 'w') as saida: # O programa deve exibir a mensagem "O número de linhas foi escrito em NOME_DO_ARQUIVO_SAIDA" ao
            saida.write(f'Número de linhas: {numero_linhas}') # finalizar a escrita do arquivo de saída.
        
        print(f'O número de linhas foi escrito em {arquivo_saida}') # O programa deve exibir a mensagem "O arquivo NOME_DO_ARQUIVO_ENTRADA não foi encontrado."
    except FileNotFoundError: # caso o arquivo de entrada não exista.
        print(f'O arquivo {arquivo_entrada} não foi encontrado.') 

# Exemplo de uso
contar_linhas('arq2.txt', 'resultado_linhas.txt') # Exemplo de uso
