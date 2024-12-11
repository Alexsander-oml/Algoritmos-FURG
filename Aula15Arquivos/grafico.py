import graphics as gf # importa a biblioteca graphics e a renomeia para gf
import random # importa a biblioteca random

win = gf.GraphWin("Minha janela", 400, 350) # GraphWin é uma classe que cria uma janela

c = gf.Circle(gf.Point(100,150), 10) # Circle é uma classe que cria um círculo
cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white']
c.setFill('red') # fill é um atributo que preenche o círculo com a cor especificada
c.draw(win) # draw é um método que desenha o círculo na janela

# win.getMouse() # getMouse é um método que faz a janela ficar aberta até que o usuário clique em algum lugar

cont = 0
while True:
    onde_clicou = win.getMouse() # getMouse é um método que retorna a posição do clique do usuário
    print(onde_clicou.getX(), onde_clicou.getY()) # imprime a posição do clique do usuário
    nova_bolinha = gf.Circle(onde_clicou, 30) # cria um novo círculo na posição do clique do usuário
    nova_bolinha.draw(win) # desenha o novo círculo na janela
    nova_bolinha.setFill(cores[cont]) # preenche o novo círculo com a cor da lista cores
    cont += 1
    if cont == len(cores):
        cont = 0
    nova_bolinha.draw(win) # desenha o novo círculo na janela