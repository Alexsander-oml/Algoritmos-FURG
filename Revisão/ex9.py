# 9) Faça um programa em Python para jogar o “jogo da velha”. O algoritmo deve permitir que
# dois jogadores joguem uma partida, usando o computador para ver o tabuleiro. Cada
# jogador vai alternadamente informando a posição onde deseja colocar a sua peça (‘O’ ou
# ‘X’). O programa deverá impedir jogadas inválidas, e determinar automaticamente quando o
# jogo terminou, e quem foi o vencedor (jogador1 ou jogador2). A cada nova jogada, o
# programa deve atualizar a situação do tabuleiro na tela.

# C1 | C2 | C3
# ---------
# C4 | C5 | C6
# ---------
# C7 | C8 | C9
V = True
while V == True:
    tabuleiro = [' ']*9
    print('''
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    ''')
    for i in range(9):
        if i % 2 == 0:
            jogada = input('Jogador 1, informe a posição que deseja jogar: ')
            if tabuleiro[int(jogada)-1] == ' ':
                tabuleiro[int(jogada)-1] = 'X'
            else:
                print('Jogada inválida')
                continue
        else:
            jogada = input('Jogador 2, informe a posição que deseja jogar: ')
            if tabuleiro[int(jogada)-1] == ' ':
                tabuleiro[int(jogada)-1] = 'O'
            else:
                print('Jogada inválida')
                continue
        print('''
        {} | {} | {}
        ---------
        {} | {} | {}
        ---------
        {} | {} | {}
        '''.format(*tabuleiro))
        if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 'X' or \
            tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 'X' or \
            tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 'X' or \
            tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 'X' or \
            tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 'X' or \
            tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 'X' or \
            tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 'X' or \
            tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 'X':
            print('Jogador 1 venceu!')
            V = False
            break
        elif tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 'O' or \
            tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 'O' or \
            tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 'O' or \
            tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 'O' or \
            tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 'O' or \
            tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 'O' or \
            tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 'O' or \
            tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 'O':
            print('Jogador 2 venceu!')
            V = False
            break

        elif ' ' not in tabuleiro:
            print('Empate!')
            V = False
            break
