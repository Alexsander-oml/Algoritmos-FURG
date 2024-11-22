arq = open('processo.txt', 'r')

# arq = ponteiro
# open = função que abre o arquivo
# 'processo.txt' = nome do arquivo
# 'r' = modo de abertura do arquivo (r = read, w = write, a = append)

print(arq)
# texto = arq.read()
# read = lê o arquivo e retorna o conteúdo do arquivo
# print(texto)
# print('----------')

lista = arq.readlines()
print(lista)

#readLines = lê o arquivo e retorna uma lista com as linhas do arquivo

arq.close()