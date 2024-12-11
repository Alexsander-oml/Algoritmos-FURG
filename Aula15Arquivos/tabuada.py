#gere as tabuadas de 0 a N em html (com tabelas) e salve em arquivo.html
'''
with open ('tabuada.html', 'w') as arq:
    arq.write('<html>\n')
    arq.write('<head>\n')
    arq.write('<title>Tabuada</title>\n')
    arq.write('</head>\n')
    arq.write('<body>\n')
    arq.write('<table border="1">\n')
    valor = int(input('Digite o número para gerar a tabuada: ')) # pegar o valor do usuário
    for i in range(valor+1): # gerar a tabuada
        arq.write('<tr>\n')
        for j in range(11): # gerar a tabuada
            arq.write('<td>{0} x {1} = {2}</td>\n'.format(i, j, i*j)) # escrever a tabuada
        arq.write('</tr>\n')
    arq.write('</table>\n')
    arq.write('</body>\n')
    arq.write('</html>\n')

print('Tabuada gerada com sucesso!')
'''

# Jeito do prisco

N = int(input('Digite o número para gerar a tabuada: '))
saida = "O resultado da tabuada é: <hr>\n"

for um_n in range(N+1):
    saida += '<table border=1>\n'
    for i in range(11):
        mult = i * N
        saida += f'<tr><td>{um_n} x {i} = {mult}</td></tr>\n'
    saida += '</table><br>'
   
with open('tabuada.html', 'w') as arq:
  arq.write(saida)

print('Tabuada gerada com sucesso!')