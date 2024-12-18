import graphics as gf  #trazer o arquivo da graphics
import random as rd 
import math as mt
rd.seed()

def foi_no_botao(botao, onde_cliquei):
    bt_x = botao.getP1().getX()
    bt_y = botao.getP1().getY()
    bt2_x = botao.getP2().getX()
    bt2_y = botao.getP2().getY()
    print(f'----> ({bt_x},{bt_y})({bt2_x},{bt2_y})')
    #print('Diagonal do botão: botao.getP1')
    return True

def abs(x):
    if x < 0:
     return x * -1
    return x

win = gf.GraphWin("Minha Janela", 400, 350)  # cria uma janela
c = gf.Circle(gf.Point(100, 150), 10)  # cria o ponto
c.setFill('red')
c.draw(win)  # fala em qual janela o ponto deve ser draw
cores = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'pink']

bolinhas = [c]  # lista para armazenar todas as bolinhas e o ponto
raio = 10 # raio do círculo que eh 10 pq o círculo tem 10 de raio

botao = gf.Rectangle(gf.Point(10, 10), gf.Point(50, 30))  # cria um botão
botao.draw(win)  # desenha o botão


while True:
     onde_cliquei = win.getMouse() # pega o ponto onde foi clicado
     print(onde_cliquei.getX(), onde_cliquei.getY()) # mostra onde foi clicado
     
     if foi_no_botao(botao, onde_cliquei):
        botao.setFill('red')
     else:
        botao.setFill('green')

     for bolinha in bolinhas:
          dx = abs(bolinha.getCenter().getX() - onde_cliquei.getX()) # diferença entre os pontos e  o centro da bolinha
          dy = abs(bolinha.getCenter().getY() - onde_cliquei.getY()) # getCenter pega o centro da bolinha do getY e getX 
          d = mt.sqrt(dx * dx + dy * dy) # teorema de pitágoras
          if d <= raio:   # se a distância for menor ou igual ao raio do círculo
                win.close()
                print("Fim do Programa")
                exit() # fecha o programa
     
     nova_bolinha = gf.Circle(onde_cliquei, 10)
     cor = rd.randint(0, len(cores) - 1)
     nova_bolinha.setFill(cores[cor])
     nova_bolinha.draw(win)
     
     bolinhas.append(nova_bolinha)  # adiciona a nova bolinha à lista
