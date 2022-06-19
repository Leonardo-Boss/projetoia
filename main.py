from classes.Agente import Agente
import os
from time import sleep

agente = Agente("mapas/labirinto1.pbm", 729)

while(agente.mover() != 1):
    sleep(0.3)
    agente.pintarLabirinto()
