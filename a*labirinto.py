from time import sleep
import os

from numpy import Infinity

tabuleiro = [['⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','🟨\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬛\u200c','⬜\u200c','⬛\u200c','⬜\u200c'],
             ['⬜\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬛\u200c','⬜\u200c','🟥\u200c','⬜\u200c'],
             ['⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c','⬜\u200c']]

def tab(tab):
    try:
        os.system('clear')
    except:
        os.system('cls')
    for l in tab:
        for s in l:
            print(s, end='')
        print()

def way(pacman, open):
    def wayr(pacman):
        if pacman.parent != None:
            pacman.parent.updatec('🟨\u200c')
            wayr(pacman.parent)
    for s in open:
        s.updatec('🟩\u200c')
    if pacman.parent != None:
        pacman.parent.updatec('🟨\u200c')
        wayr(pacman.parent)
    

squares = ('⬛\u200c', '🟨\u200c', '🟥\u200c')

class square:
    def __init__(self, color, i, j, tabuleiro,up=None, left=None, right=None, down=None):
        self._color = color
        self.up = up
        self.left = left
        self.right = right
        self.down = down
        self.i = i
        self.j = j
        self.cost = 1
        self.e = 8-i + 8-j
        self.h = Infinity
        self.tabuleiro = tabuleiro
        self.parent = None
    def update(self, cost):
        self.cost = cost
        self.h =  self.cost + self.e
    def updatec(self, color):
        self._color = color
        self.tabuleiro[self.i][self.j] = color

grafo = {}
for l in range(1,len(tabuleiro)-1):
    temp = {}
    for s in range(len(tabuleiro[l])):
        if tabuleiro[l][s] in squares:
            temp[s] = square(tabuleiro[l][s], l, s, tabuleiro)
            if tabuleiro[l][s] == '🟨\u200c':
                initial = temp[s]
            elif tabuleiro[l][s] == '🟥\u200c':
                final = temp[s]
    grafo[l] = temp

# grafo = {l: {s: square(tabuleiro[l][s], l, s, tabuleiro) for s in range(len(tabuleiro[l])) if tabuleiro[l][s] in squares} for l in range(1,len(tabuleiro)-1)}

for i, l in grafo.items():
    for j, s in l.items():
        if tabuleiro[i-1][j] in squares :
            grafo[i][j].up = grafo[i-1][j]
        if tabuleiro[i][j-1] in squares:
            grafo[i][j].left = grafo[i][j-1]
        if tabuleiro[i][j+1] in squares:
            grafo[i][j].right = grafo[i][j+1]
        if tabuleiro[i+1][j] in squares:
            grafo[i][j].down = grafo[i+1][j]

pacman = initial
cereja = final
open = []
closed = []
while pacman != final:
    path = pacman.cost + 1
    if pacman not in open:
        open.append(pacman)
    if pacman.down and pacman.down and pacman.parent != pacman.down and pacman.down not in open:
        ocost = pacman.down.cost
        oh = pacman.down.h
        pacman.down.update(path)
        if oh > pacman.down.h:
            pacman.down.updatec('🟦\u200c')
            pacman.down.parent = pacman
            closed.append(pacman.down)
        else:
            pacman.down.update(ocost)
    if pacman.up and pacman.up and pacman.parent != pacman.up and pacman.up not in open:
        ocost = pacman.up.cost
        oh = pacman.up.h
        pacman.up.update(path)
        if oh > pacman.up.h:
            pacman.up.updatec('🟦\u200c')
            pacman.up.parent = pacman
            closed.append(pacman.up)
        else:
            pacman.up.update(ocost)
    if pacman.left and pacman.left and pacman.parent != pacman.left and pacman.left not in open:
        ocost = pacman.left.cost
        oh = pacman.left.h
        pacman.left.update(path)
        if oh > pacman.left.h:
            pacman.left.updatec('🟦\u200c')
            pacman.left.parent = pacman
            closed.append(pacman.left)
        else:
            pacman.left.update(ocost)
    if pacman.right and pacman.right and pacman.parent != pacman.right and pacman.right not in open:
        ocost = pacman.right.cost
        oh = pacman.right.h
        pacman.right.update(path)
        if oh > pacman.right.h:
            pacman.right.updatec('🟦\u200c')
            pacman.right.parent = pacman
            closed.append(pacman.right)
        else:
            pacman.right.update(ocost)
    if pacman in closed:
        closed.remove(pacman)
    tab(tabuleiro)
    closed.sort(key=lambda square:square.h)
    pacman.updatec('🟩\u200c')
    pacman = closed[0]
    pacman.updatec('🟨\u200c')
    way(pacman,open)
    sleep(0.5)
tab(tabuleiro)