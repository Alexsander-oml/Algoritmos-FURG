import os
import json
import csv

# Operações básicas com arquivos em Python

# Abrindo um arquivo
arquivo = open('exemplo.txt', 'w')  # modo 'w' é para escrita
arquivo.write('Olá, mundo!\n')
arquivo.close()

# Lendo de um arquivo
arquivo = open('exemplo.txt', 'r')  # modo 'r' é para leitura
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Adicionando a um arquivo
arquivo = open('exemplo.txt', 'a')  # modo 'a' é para adicionar
arquivo.write('Adicionando uma nova linha.\n')
arquivo.close()

# Lendo linha por linha
arquivo = open('exemplo.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

# Usando a declaração 'with' (recomendado)
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Operações avançadas com arquivos

# Lendo e escrevendo arquivos binários
with open('exemplo.bin', 'wb') as arquivo:
    arquivo.write(b'\x00\x01\x02\x03')

with open('exemplo.bin', 'rb') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Trabalhando com caminhos de arquivos

# Obter o diretório de trabalho atual
cwd = os.getcwd()
print('Diretório de trabalho atual:', cwd)

# Listar arquivos em um diretório
arquivos = os.listdir(cwd)
print('Arquivos no diretório:', arquivos)

# Verificar se um arquivo existe
arquivo_existe = os.path.isfile('exemplo.txt')
print('O arquivo exemplo.txt existe?', arquivo_existe)

# Deletando um arquivo
if arquivo_existe:
    os.remove('exemplo.txt')
    print('exemplo.txt foi deletado')

# Trabalhando com arquivos JSON

dados = {'nome': 'João', 'idade': 30, 'cidade': 'Nova York'}

# Escrevendo JSON em um arquivo
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)

# Lendo JSON de um arquivo
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)

# Trabalhando com arquivos CSV

# Escrevendo em um arquivo CSV
with open('dados.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Nome', 'Idade', 'Cidade'])
    escritor.writerow(['João', 30, 'Nova York'])
    escritor.writerow(['Ana', 25, 'Los Angeles'])

# Lendo de um arquivo CSV
with open('dados.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)