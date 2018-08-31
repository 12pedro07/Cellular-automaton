import numpy as np
import random
import time

figure = 'glider'
sizex = 50
sizey = 150
board = np.zeros((sizex, sizey), dtype=np.str)
nxt = np.zeros((sizex, sizey), dtype=np.str)

def manual():
    for x in range(sizex-1):
        for y in range(sizey-1):
            board[x][y] = ' '
    if figure == 'glider':
        board[10][10] = 'X'
        board[11][10] = 'X'
        board[12][10] = 'X'
        board[12][9] = 'X'
        board[11][8] = 'X'
    elif figure == 'line':
        board[10][10] = 'X'
        board[11][10] = 'X'
        board[12][10] = 'X'
    elif figure == 'block':
        board[10][10] = 'X'
        board[10][11] = 'X'
        board[11][10] = 'X'
        board[11][11] = 'X'

def rand():
    for x in range(sizex-1):
        for y in range(sizey-1):
            aux = random.uniform(0,1)
            if aux >= 0.9:
                board[x][y] = 'X'
            else:
                board[x][y] = ' '


def np2string():
    string = ''
    for m in range(sizex):
        for n in range(sizey):
            if n == sizey-1:
                string = string + board[m][n]
                string = string + '\n'
            else:
                string = string + board[m][n]
    return string


def vizinhos(i, j): # Funcionando perfeitamente
    neighbors = 0
    if i == 0 or j == 0 or i == sizex-1 or j == sizey-1:
        return neighbors
    if board[i-1][j] == 'X':
        neighbors+=1 # cima
        # print('cima/')
    if board[i+1][j] == 'X':
        neighbors+=1 # baixo
        # print('baixo/')
    if board[i][j-1] == 'X':
        neighbors+=1 # esquerda
        # print('esquerda/')
    if board[i][j+1] == 'X':
        neighbors+=1 # direita
        # print('direita/')
    if board[i-1][j+1] == 'X':
        neighbors+=1 # diagonal direita em cima
        # print('dir_cima/')
    if board[i-1][j-1] == 'X':
        neighbors+=1 # diagonal esquerda em cima
        # print('esq_cima/')
    if board[i+1][j+1] == 'X':
        neighbors+=1 # diagonal direita em baixo
        # print('dir_baixo/')
    if board[i+1][j-1] == 'X':
        neighbors+=1 # diagonal esquerda em baixo
        # print('esq_baixo/')
    return neighbors

rand()
np2string()

while True:
    print_b = np2string()
    print(print_b)
    print('\n'*5)
    # Regras:
    for i in range(sizex):
        for j in range(sizey):
            # print ("\nboard[%i][%i]" %(x, y)) # TESTANDO MATRIZ
            neighbors = vizinhos(i, j)
            # if i <= 13 and i >= 9 and j>=8 and j<=12:
            #     print('10 9 = '+str(board[10][9]))
            #     print(('cell[%i][%i] = '%(i, j))+str(neighbors))
            #     print('\n')
            # print(neighbors)
            if ((board[i][j] == 'X') and (neighbors < 2)):
                nxt[i][j] = ' '
            elif ((board[i][j] == 'X') and (neighbors > 3)):
                nxt[i][j] = ' '
            elif ((board[i][j] == ' ') and (neighbors == 3)):
                nxt[i][j] = 'X'
            else:
                nxt[i][j] = board[i][j]

    board = nxt.copy() # sem o .copy() ele simplesmente muda o nome de nxt para board e buga a funcionalidade do codigo
    time.sleep(.2)
