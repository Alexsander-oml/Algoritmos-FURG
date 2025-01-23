# Jogo da Velha sem funções

# Inicializa o tabuleiro
tabuleiro = [' ' for _ in range(9)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    for i in range(3):
        print(f"{tabuleiro[3*i]} | {tabuleiro[3*i+1]} | {tabuleiro[3*i+2]}")
        if i < 2:
            print("--+---+--")

# Função para verificar se há um vencedor
def verificar_vencedor():
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] != ' ':
            return tabuleiro[combinacao[0]]
    return None

# Função principal do jogo
def jogar():
    jogador_atual = 'X'
    for _ in range(9):
        imprimir_tabuleiro()
        print(f"Jogador {jogador_atual}, escolha uma posição (1-9):")
        while True:
            try:
                posicao = int(input()) - 1
                if tabuleiro[posicao] == ' ':
                    tabuleiro[posicao] = jogador_atual
                    break
                else:
                    print("Posição já ocupada. Escolha outra posição.")
            except (ValueError, IndexError):
                print("Entrada inválida. Escolha uma posição de 1 a 9.")
        
        vencedor = verificar_vencedor()
        if vencedor:
            imprimir_tabuleiro()
            print(f"Jogador {vencedor} venceu!")
            return
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    
    imprimir_tabuleiro()
    print("Empate!")

# Inicia o jogo
jogar()




# Jogo da Velha sem funções

# Inicializa o tabuleiro
tabuleiro = [' ' for _ in range(9)]

# Variável para controlar o jogador atual
jogador_atual = 'X'

# Loop principal do jogo
for _ in range(9):
    # Imprime o tabuleiro
    for i in range(3):
        print(f"{tabuleiro[3*i]} | {tabuleiro[3*i+1]} | {tabuleiro[3*i+2]}")
        if i < 2:
            print("--+---+--")
    
    # Solicita a posição ao jogador
    print(f"Jogador {jogador_atual}, escolha uma posição (1-9):")
    while True:
        try:
            posicao = int(input()) - 1
            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador_atual
                break
            else:
                print("Posição já ocupada. Escolha outra posição.")
        except (ValueError, IndexError):
            print("Entrada inválida. Escolha uma posição de 1 a 9.")
    
    # Verifica se há um vencedor
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    vencedor = None
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] != ' ':
            vencedor = tabuleiro[combinacao[0]]
            break
    
    if vencedor:
        # Imprime o tabuleiro final
        for i in range(3):
            print(f"{tabuleiro[3*i]} | {tabuleiro[3*i+1]} | {tabuleiro[3*i+2]}")
            if i < 2:
                print("--+---+--")
        print(f"Jogador {vencedor} venceu!")
        break
    
    # Alterna o jogador
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
else:
    # Imprime o tabuleiro final em caso de empate
    for i in range(3):
        print(f"{tabuleiro[3*i]} | {tabuleiro[3*i+1]} | {tabuleiro[3*i+2]}")
        if i < 2:
            print("--+---+--")
    print("Empate!")