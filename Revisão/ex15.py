# 15) Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade,
# em um determinado dia. Em um arquivo texto é fornecido, para cada casa visitada, o
# número do canal (4, 5, 7, 12) e o número de pessoas que o estavam assistindo naquela casa,
# separados por ponto e vírgula. Se a televisão estivesse desligada, nada era anotado, ou seja,
# esta casa não entrava na pesquisa. Faça uma função, em Python, que receba dois
# parâmetros, o nome do arquivo com os dados e o número do canal, e retorne a
# porcentagem de audiência deste canal.

def audience(archive, channel):
    arq = open(archive, "r") #  'r' significa que o arquivo será aberto para leitura
    lines = arq.readlines() # Lê todas as linhas do arquivo e as armazena em uma lista
    
    channelNum = channel # Canal que será pesquisado
    channelCount = 0 # Contador de pessoas assistindo ao canal
    totalSum = 0 # Contador de pessoas assistindo a todos os canais
    
    for i in lines: # Para cada linha do arquivo
        totalSum+=int(i.split(";")[1]) # Adiciona o número de pessoas assistindo ao canal ao contador total
        if i.split(";")[0] == channelNum: # Se o canal da linha for igual ao canal pesquisado
            channelCount+=int(i.split(";")[1]) # Adiciona o número de pessoas assistindo ao canal ao contador do canal pesquisado
    return (channelCount*100)/totalSum # Retorna o percentual de audiência do canal pesquisado

percent = audience("ex15.txt", "12") # Chama a função audience com os parâmetros "ex15.txt" e "12" e armazena o retorno na variável percent

print(f"O percentual de audiencia é de {percent:,.2f}%")
