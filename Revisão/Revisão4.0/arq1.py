# Crie uma função que receba o nome de um arquivo de entrada e 
# de um arquivo de saída. O arquivo de entrada contém um texto com várias palavras. 
# O programa deve contar o número de palavras do texto e escrever esse número no arquivo de 
# saída. Caso o arquivo de entrada não exista, o programa deve exibir uma mensagem de erro.


def contar_palavras(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as entrada:
            texto = entrada.read()
            palavras = texto.split()
            numero_palavras = len(palavras)
        
        with open(arquivo_saida, 'w') as saida:
            saida.write(f'Número de palavras: {numero_palavras}')
        
        print(f'O número de palavras foi escrito em {arquivo_saida}')
    except FileNotFoundError:
        print(f'O arquivo {arquivo_entrada} não foi encontrado.')

# Exemplo de uso
contar_palavras('arq1.txt', 'resultado.txt')
