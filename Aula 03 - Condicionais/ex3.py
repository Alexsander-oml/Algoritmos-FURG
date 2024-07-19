nome = input('Digite seu nome: ')
hora = float(input('Digite a hora atual:' ))
if hora <= 12 and hora >= 6:
 print('Bom dia,',nome)
if hora > 12 and hora <= 18:
 print('Boa tarde',nome)
if hora > 18 and hora <= 24:
 print('Boa noite',nome)
if hora >= 0 and hora <= 5:
 print('Boa madrugada',nome)