with open ('nome', 'r') as arq: # abre o arquivo para leitura
    string = arq.read() # lê o arquivo
    print(string) # imprime a string


arq.write(string) # escreve a string no arquivo


arq.seek(offset, Local) # move o cursor para a posição offset a partir do Local

arq.seek(local) # move o cursor para o local

ex: arq.seek(0) # move o cursor para o início do arquivo