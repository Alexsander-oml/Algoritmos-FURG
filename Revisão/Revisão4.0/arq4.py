# PROGRAMA QUE ANALISA UM TEXTO E ESCREVE O NÚMERO DE LINHAS, PALAVRAS E CARACTERES EM UM ARQUIVO DE SAÍDA

def analisar_texto(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as entrada:
            texto = entrada.read()
            linhas = texto.splitlines()
            palavras = texto.split()
            caracteres = len(texto.replace(" ", ""))
            numero_linhas = len(linhas)
            numero_palavras = len(palavras)
        
        with open(arquivo_saida, 'w') as saida:
            saida.write(f'Número de linhas: {numero_linhas}\n')
            saida.write(f'Número de palavras: {numero_palavras}\n')
            saida.write(f'Número de caracteres (excluindo espaços): {caracteres}\n')
        
        print(f'Os resultados foram escritos em {arquivo_saida}')
    except FileNotFoundError:
        print(f'O arquivo {arquivo_entrada} não foi encontrado.')

# Exemplo de uso
analisar_texto('arq4.txt', 'resultado_analise.txt')
