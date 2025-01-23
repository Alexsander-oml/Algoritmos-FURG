# 14) Um anagrama é uma espécie de jogo de palavras, resultando do rearranjo das letras de
# uma palavra ou frase para produzir outras palavras, utilizando todas as letras originais
# exatamente uma vez. Um exemplo conhecido é o nome da personagem “Iracema”, um
# anagrama de “América”, no romance de José de Alencar. Escreva um programa, em Python,
# para ler um valor N correspondente ao número de palavras a serem informadas. Após, ler as
# N palavras, e dizer se formam um anagrama. Considerar 1 <= N <= 5, e palavras com, no
# máximo, 10 caracteres.

def sao_anagramas(palavras):
    sorted_palavras = [''.join(sorted(palavra)) for palavra in palavras]
    return all(palavra == sorted_palavras[0] for palavra in sorted_palavras)

palavras = []
C = 0
V = True

while C < 5 and V:
    aux = input("Digite as palavras com no máximo 10 caracteres: ").upper()
    if len(aux) <= 10:
        palavras.append(aux)
        C += 1
        print(f'Lista: {palavras}')
        if C > 1:
            if sao_anagramas(palavras):
                print("As palavras são anagramas.")
            else:
                print("As palavras não são anagramas.")
        aux2 = input("Deseja adicionar mais uma palavra? [Y/N]: ").upper()
        if aux2 == "N" or aux2 != 'Y':
            V = False
    else:
        print("A palavra deve conter apenas 10 caracteres!!")

