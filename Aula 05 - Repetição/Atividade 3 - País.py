P = input('Adivinhe o país').lower()
C = 0
while C != 'brasil':
 if C == 1:
  print('continente": América do Sul')
 if C == 2:
  print('area: "8,515,767 km²'
 if C == 3:
  print('Maior país da América do Sul e o quinto maior do mundo em área.'
 if C == 3:
  print('clima: "Tropical')
 C+=1
print('acabou')




paises = {
    "Brasil": {
        "capital": "Brasília",
        "lingua": "Português",
        "continente": "América do Sul",
        "area": "8,515,767 km²",
        "populacao": "213 milhões",
        "moeda": "Real",
        "fuso_horario": "UTC-3",
        "gastronomia": "Feijoada",
        "principais_cidades": ["São Paulo", "Rio de Janeiro", "Salvador"],
        "historia_curiosa": "O Brasil é o maior país da América do Sul e o quinto maior do mundo em área.",
        "clima": "Tropical"
    },
    "França": {
        "capital": "Paris",
        "lingua": "Francês",
        "continente": "Europa",
        "area": "551,695 km²",
        "populacao": "67 milhões",
        "moeda": "Euro",
        "fuso_horario": "UTC+1",
        "gastronomia": "Croissant",
        "principais_cidades": ["Marseille", "Lyon", "Toulouse"],
        "historia_curiosa": "A Torre Eiffel, um dos monumentos mais famosos do mundo, foi inicialmente criticada por muitos franceses.",
        "clima": "Temperado"
    },
    # Adicione mais países conforme necessário
}
