'''
#Leia o arquivo alunos.csv e mostre o conteudo do arquivo

arq = open('alunos.csv', 'r')

print(arq)
texto = arq.read()
print(texto)


arq.close()

#Liste apneas os nomes dos Alunos

arq = open('alunos.csv', 'r')

lista = arq.readlines()

for linha in lista:
    colunas = linha.split(';')
    print(colunas[1])
    print('----------')
'''

'''
Jeito do Prisco
'''

'''
#[:1] = pega a primeira linha
arq = open('alunos.csv', 'r')
tudo = arq.readlines()

for linha in tudo[1:]:
    uma_lista = linha.split(';')   
    print(uma_lista[1])

arq.close()
'''
#Mostre quem é o aluno mais novo

def mostra_nomes(lista):
    for linha in lista:
        uma_lista = linha.split(';')
        print(uma_lista[1])
        print('----------')

def mais_novo(lista): #pega a lista e retorna o nome e a data de nascimento do aluno mais novo
   novo = '10251231' #calibrar o novo
   nome_do_novo = ''
   dt_original = ''
   for linha in lista[1:]: #[1:] = pula a primeira linha #for linha in lista[1:]: = para cada linha na lista a partir da segunda linha
        uma_lista = linha.split(';') #split = separa os elementos da linha e cria uma lista 
        data = uma_lista[2][:-1] #[:-1] = pega tudo menos o último caractere tirando o \n
        lista_data = data.split('/')
        data_f = lista_data[2] + lista_data[1] + lista_data[0]
        if data_f > novo:
            novo = data_f
            nome_do_novo = uma_lista[1]
            dt_original = data
    print(nome_do_novo, dt_original)
    


arq = open('alunos.csv', 'r')
tudo = arq.readlines() #readlines = lê o arquivo e retorna uma lista com as linhas do arquivo
mostra_nomes(tudo)
mais_novo(tudo)
arq.close()



'''
def mostra_nomes(lista):
    for linha in lista:
        uma_lista = linha.split(';')
        print(uma_lista[1])
        print('----------')

def mais_novo(lista): #pega a lista e retorna o nome e a data de nascimento do aluno mais novo
    for linha in lista[1:]: #[1:] = pula a primeira linha #for linha in lista[1:]: = para cada linha na lista a partir da segunda linha
        uma_lista = linha.split(';') #split = separa os elementos da linha e cria uma lista 
        data = uma_lista[2][:-1] #[:-1] = pega tudo menos o último caractere tirando o \n
        print(data)

        dia, mes, ano = data.split('/')
        dataf = f'{ano}/{mes}/{dia}'
        print(dia, mes, ano)
        print('----------')

        if ano < menor:
            menor = ano
            nome = uma_lista[1]
    print(nome, menor)
    print(dataf)


arq = open('alunos.csv', 'r')
tudo = arq.readlines() #readlines = lê o arquivo e retorna uma lista com as linhas do arquivo
#mostra_nomes(tudo)
mais_novo(tudo)
arq.close()
'''


''' 
Matricula;Nome;Nascimento
171079;Emylly;15/04/2001
169592;Davi;09/02/2006
169622;Alex;25/06/2003
169590;Marcos;15/11/2001
28155;André;23/03/1981 
'''

'''
arq = open('alunos.csv', 'r')
arq = arq.readlines()
arq = arq[1:]

menor = 999
for linha in arq:
    colunas = linha.split(';')
    nascimento = colunas[2]
    nascimento = nascimento.strip()
    nascimento = nascimento[0:4]
    nascimento = int(nascimento)
    if nascimento > menor:
        menor = nascimento
        nome = colunas[1]
print(nome, menor)
'''

