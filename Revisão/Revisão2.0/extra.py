# 1) (5 Pontos) Considere um programa em Python que simula um jogo de cartas com um
#  baralho completo. O baralho é inicializado com 52 cartas, divididas em 4 naipes
#  (Paus, Ouros, Copas e Espadas) e 13 valores (de 2 a 10, Valete, Dama, Rei e Ás). O
#  programa deve utilizar listas para armazenar o baralho e sortear duas cartas para
#  cada um de 6 jogadores. Mostre na tela cada uma das cartas sorteadas para cada
#  jogador. Você não deve permitir que uma carta seja sorteada mais de uma vez.

import random

# Criação do baralho
baralho = []
naipes = ["Paus", "Ouros", "Copas", "Espadas"]
valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás"]

for naipe in naipes:
    for valor in valores:
        baralho.append(valor + " de " + naipe)

# Sorteio das cartas
jogadores = []
for i in range(6):
    jogador = []
    for j in range(2):
        carta = random.choice(baralho)
        jogador.append(carta)
        baralho.remove(carta)
    jogadores.append(jogador)

# Mostrar as cartas sorteadas
for i, jogador in enumerate(jogadores):
    print(f"Jogador {i + 1}: {jogador[0]} e {jogador[1]}")

#      2) (5 Pontos) O Instagram é uma popular plataforma de mídia social que permite aos
#  usuários compartilhar fotos e vídeos. Considere um cenário em que você está
#  desenvolvendo uma funcionalidade para analisar os comentários em postagens do
#  Instagram.
#  a) Escreva um código em Python que verifique se uma string comentário contém a
#  menção a um usuário. Uma menção começa com o símbolo "@" seguido por um
#  nome de usuário válido (composto apenas por letras minúsculas e números), por
#  exemplo: "@usuario123".
#  b) Escreva um código em Python que substitua todas as menções a usuários na string
#  comentário por "USUARIO_MENCIONADO".
#  c) Dado um conjunto de palavras proibidas, escreva um código em Python que
#  verifique se a string comentário contém alguma das palavras proibidas. Se contiver,
#  exiba "Conteúdo inadequado", caso contrário, exiba "Comentário permitido"

# a) Verificar menção a usuário
def verificarMencao(comentario):
    if "@" in comentario:
        return True
    return False

# b) Substituir menções a usuários
def substituirMencao(comentario):
    return comentario.replace("@", "USUARIO_MENCIONADO")

# c) Verificar palavras proibidas
def verificarPalavrasProibidas(comentario, palavrasProibidas):
    for palavra in palavrasProibidas:
        if palavra in comentario:
            return "Conteúdo inadequado"
    return "Comentário permitido"

# Testes
comentario = "Olá, @usuario123! Como você está? #feliz"
print(verificarMencao(comentario))
print(substituirMencao(comentario))
print(verificarPalavrasProibidas(comentario, ["feliz", "triste"]))

# 3) (5 Pontos) Considere um programa em Python que simula um jogo de dados. O jogo
#  consiste em lançar dois dados e somar os valores obtidos. O jogador ganha se a soma
#  for 7 ou 11 e perde se a soma for 2, 3 ou 12. Em qualquer outro caso, o jogador
#  continua jogando até obter a mesma soma inicial ou uma soma de 7. Escreva um
#  programa em Python que simule esse jogo e exiba se o jogador ganhou ou perdeu.

import random

def lancar_dado():
    return random.randint(1, 6)

def main():

    # Lançar os dados
    dado1 = lancar_dado()
    dado2 = lancar_dado()
    soma = dado1 + dado2

    # Verificar o resultado
    if soma == 7 or soma == 11:
        print(f"Você ganhou! Soma: {soma}")
    elif soma == 2 or soma == 3 or soma == 12:
        print(f"Você perdeu! Soma: {soma}")
    else:
        print(f"Continue jogando! Soma: {soma}")
        while True:
            dado1 = lancar_dado()
            dado2 = lancar_dado()
            nova_soma = dado1 + dado2
            if nova_soma == soma:
                print(f"Você ganhou! Soma: {nova_soma}")
                break
            elif nova_soma == 7:
                print(f"Você perdeu! Soma: {nova_soma}")
                break
            else:
                print(f"Continue jogando! Soma: {nova_soma}")

# Executar o programa
main()

# 4) (5 Pontos) Considere um programa em Python que simula um jogo de adivinhação. O
#  computador escolhe um número aleatório entre 1 e 100 e o jogador tenta adivinhar
#  qual é esse número. O computador informa se o número escolhido é maior ou menor
#  que o número escolhido pelo jogador. O jogo termina quando o jogador acerta o
#  número ou desiste. Escreva um programa em Python que simule esse jogo.

import random

def main():
    # Escolher um número aleatório
    numero = random.randint(1, 100)

    # Pedir ao jogador para adivinhar
    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))
        if palpite == numero:
            print("Parabéns! Você acertou!")
            break
        elif palpite < numero:
            print("O número é maior.")
        else:
            print("O número é menor.")

# Executar o programa
main()

# 5) (5 Pontos) Considere um programa em Python que simula um jogo de forca. O

#  computador escolhe uma palavra aleatória de um conjunto de palavras e o jogador
#  tenta adivinhar a palavra, letra por letra. O jogador tem um número limitado de
#  tentativas para adivinhar a palavra. O computador informa se a letra escolhida pelo
#  jogador está presente na palavra. Escreva um programa em Python que simule esse
#  jogo.

import random

def main():
    # Lista de palavras
    palavras = ["python", "java", "csharp", "javascript", "ruby", "php", "html", "css"]

    # Escolher uma palavra aleatória
    palavra = random.choice(palavras)

    # Inicializar a palavra a ser exibida
    palavra_exibida = ["_"] * len(palavra)

    # Número de tentativas
    tentativas = 6

    # Loop principal
    while tentativas > 0:
        # Exibir a palavra
        print(" ".join(palavra_exibida))

        # Pedir uma letra
        letra = input("Digite uma letra: ")

        # Verificar se a letra está presente na palavra
        if letra in palavra:
            print("Letra correta!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_exibida[i] = letra
        else:
            print("Letra incorreta!")
            tentativas -= 1

        # Verificar se a palavra foi adivinhada
        if "_" not in palavra_exibida:
            print("Parabéns! Você adivinhou a palavra!")
            break

    # Verificar se o jogador perdeu
    if tentativas == 0:
        print(f"Você perdeu! A palavra era {palavra}")

# Executar o programa

main()

# 6) (5 Pontos) Considere um programa em Python que simula um jogo de batalha naval.
#  O tabuleiro do jogo é uma matriz 10x10 onde cada célula representa uma posição. O
#  computador escolhe aleatoriamente a posição de um navio de tamanho 3 (horizontal
#  ou vertical) e o jogador tenta adivinhar a posição do navio. O jogador tem um
#  número limitado de tentativas para acertar a posição do navio. O computador informa
#  se o jogador acertou ou errou a posição do navio. Escreva um programa em Python
#  que simule esse jogo.

import random

def main():
    # Criar o tabuleiro
    tabuleiro = [["~" for _ in range(10)] for _ in range(10)]

    # Escolher a posição do navio
    navio_x = random.randint(0, 7)
    navio_y = random.randint(0, 7)
    orientacao = random.choice(["horizontal", "vertical"])

    if orientacao == "horizontal":
        for i in range(3):
            tabuleiro[navio_x + i][navio_y] = "O"
    else:
        for i in range(3):
            tabuleiro[navio_x][navio_y + i] = "O"

    # Número de tentativas
    tentativas = 5

    # Loop principal
    while tentativas > 0:
        # Exibir o tabuleiro
        for linha in tabuleiro:
            print(" ".join(linha))

        # Pedir a posição
        x = int(input("Digite a linha (0-9): "))
        y = int(input("Digite a coluna (0-9): "))

        # Verificar se o jogador acertou
        if tabuleiro[x][y] == "O":
            print("Você acertou!")
            break
        else:
            print("Você errou!")
            tentativas -= 1

    # Verificar se o jogador perdeu
    if tentativas == 0:
        print("Você perdeu!")

# Executar o programa
main()
