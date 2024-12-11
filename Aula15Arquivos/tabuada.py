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
saida = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabuada</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            padding: 10px;
            text-align: center;
            border: 1px solid #ddd;
        }
        th {
            background: linear-gradient(to right, #8e44ad, #9b59b6);
            color: white;
        }
        tr:nth-child(even) {
            background: linear-gradient(to right, #dcd0ff, #e6e1ff);
        }
    </style>
</head>
<body>
<h1>Tabuada</h1>
"""

for um_n in range(N+1):
    saida += '<table>\n'
    saida += '<tr><th colspan="2">Tabuada do {}</th></tr>\n'.format(um_n)
    for i in range(11):
        mult = i * um_n
        saida += f'<tr><td>{um_n} x {i}</td><td>{mult}</td></tr>\n'
    saida += '</table>\n'
   
saida += """
</body>
</html>
"""

with open('tabuada.html', 'w') as arq:
    arq.write(saida)

print('Tabuada gerada com sucesso!')