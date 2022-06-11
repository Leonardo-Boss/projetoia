from classes.Agente import Agente
import os
from time import sleep

agente = Agente("mapas/labirinto1.pbm", 1)

while(agente.mover() != 1):
    sleep(0.2)
agente.pintarLabirinto()