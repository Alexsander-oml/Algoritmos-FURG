# Crie uma função que receba o nome de um arquivo de 
# entrada e de um arquivo de saída. O arquivo de entrada contém uma string 
# com palavras separadas por espaços. A função deve escrever no arquivo de saída 
# o número de caracteres (excluindo espaços) da string contida no arquivo de entrada. 
# Caso o arquivo de entrada não exista, a função deve imprimir uma mensagem de erro.



def contar_caracteres(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as entrada:
            texto = entrada.read()
            caracteres = len(texto.replace(" ", ""))
        
        with open(arquivo_saida, 'w') as saida:
            saida.write(f'Número de caracteres (excluindo espaços): {caracteres}')
        
        print(f'O número de caracteres foi escrito em {arquivo_saida}')
    except FileNotFoundError:
        print(f'O arquivo {arquivo_entrada} não foi encontrado.')

# Exemplo de uso
contar_caracteres('arq3.txt', 'resultado_caracteres.txt')
