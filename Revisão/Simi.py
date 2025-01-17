def calculo_similaridade(string1, string2):
    maxC = max(len(string1), len(string2))
    minC = min(len(string1), len(string2))

    iguais = 0

    for i in range(minC):
        if string1[i] == string2[i]:
            iguais+=1
        
    similaridade = (iguais/maxC) * 100
    return round(similaridade, 2)

string1 = "csa"
string2 = "casa"
similaridade = calculo_similaridade(string1, string2)
print(f'A similaridade entre {string1} e {string2} é {similaridade}')