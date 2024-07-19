nome = input("Digite seu nome: ")
hora = float(input("Digite a hora atual:"))
if hora <= 12 and hora >= 6:
    print("Bom dia,", nome)
if hora > 12 and hora <= 18:
    print("Boa tarde", nome)
if hora > 18 and hora <= 24:
    print("Boa noite", nome)
if hora >= 0 and hora <= 5:
    print("Boa madrugada", nome)


    """
nome = input('Digite seu nome: ')
hora = float(input('Digite a hora atual:' ))

if hora > 12:
    if hora > 18:
        saudacao = 'boa noite'
        else:
            saudacao = 'boa tarde'
            else:
                if hora > 5: 
                saudacao = 'boa dia'
                else:
                    saudacao = 'boa noite'
  print(f'{saudacao},{nome})

  
  if hora > 6 and hora < 12:
   saudacao = 'bom dia'
   else:
   if hora > 12 and hora < 18:
     saudacao = 'Boa tarde'
    else:
      saudacao = 'Boa noite'
 """
