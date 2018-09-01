import time
import random
from p5 import *
import numpy as np

#################################################################
#                                                               #
#   ADAPTAÇÃO DO GAME OF LIFE PARA O TERMINAL UTILIZANDO O P5   #
#                     (NADA OTIMIZADO)                          #
#                                                               #
#################################################################

w = 15
cols = floor((2000/w))
rows = floor((1000/w))
board = np.zeros((cols, rows), dtype=np.str)
nxt = np.zeros((cols, rows), dtype=np.str)
casas = []
cont = 0

def rand():
    for x in range(cols):
        for y in range(rows):
            aux = random.uniform(0,1)
            if aux >= 0.88:
                board[x][y] = 'X'
            else:
                board[x][y] = ' '

def np2string():
    string = ''
    for m in range(cols):
        for n in range(rows):
            if n == rows-1:
                string = string + board[m][n]
                string = string + '\n'
            else:
                string = string + board[m][n]
    return string

def vizinhos(i, j):
    neighbors = 0
    if i == 0 or j == 0 or i >= cols-2 or j >= rows-2 : return neighbors
    if board[i-1][j] == 'X' : neighbors+=1 # cima
    if board[i+1][j] == 'X' : neighbors+=1 # baixo
    if board[i][j-1] == 'X' : neighbors+=1 # esquerda
    if board[i][j+1] == 'X' : neighbors+=1 # direita
    if board[i-1][j+1] == 'X' : neighbors+=1 # diagonal direita em cima
    if board[i-1][j-1] == 'X' : neighbors+=1 # diagonal esquerda em cima
    if board[i+1][j+1] == 'X' : neighbors+=1 # diagonal direita em baixo
    if board[i+1][j-1] == 'X' : neighbors+=1 # diagonal esquerda em baixo
    return neighbors

rand()
np2string()

def setup():
    size(1920,1080) # tamanho da tela
    global grid
    grid = [[] for z in range(rows)]
    for i in range(rows):
        for j in range(cols):
            cell = Cell(i,j)
            casas.append(cell)

    item = 0;
    for i in range(rows):
        for j in range(cols):
            grid[i].append(casas[item])
            item = item + 1

def draw():
    global board
    background(51)

    ################ NOT P5 ################
    # Regras:
    for i in range(cols):
        for j in range(rows):
            neighbors = vizinhos(i, j)
            if ((board[i][j] == 'X') and (neighbors < 2)):
                nxt[i][j] = ' '
            elif ((board[i][j] == 'X') and (neighbors > 3)):
                nxt[i][j] = ' '
            elif ((board[i][j] == ' ') and (neighbors == 3)):
                nxt[i][j] = 'X'
            else:
                nxt[i][j] = board[i][j]

    board = nxt.copy() # sem o .copy() ele simplesmente muda o nome de nxt para board e buga a funcionalidade do codigo
    ########################################

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #print('grid', len(grid), len(grid[i]), i, j)
            #print('board', len(board), len(board[i]), i, j)
            [grid[i][j].die() if board[j][i] == ' ' else grid[i][j].live()]


    for i in range(len(casas)):
        casas[i].show()

class Cell:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        cor = random_uniform(0,1)
        if cor < 0.5:
            cor = 255
        else:
            cor = 0
        self.color = cor

    def show(self):
        x = self.j*w
        y = self.i*w
        stroke(150)
        fill(self.color,self.color,self.color) # fill( R, G, B, alpha )
        square((x,y),w)
        no_fill()

    def live(self):
        self.color = 0

    def die(self):
        self.color = 255


run()
