from classes.Agente import Agente
from classes.Labirinto import Labirinto
import os
from time import sleep

l = Labirinto("mapas/labirinto1.pbm")
agente = Agente(l)

while(agente.mover() != 0):
    os.system('clear')
    print(l)
    sleep(0.3)