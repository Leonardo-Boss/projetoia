from classes.Agente import Agente
from time import sleep

from classes.Labirinto import Labirinto

labirinto = Labirinto("mapas/labirinto1.pbm")

agente = Agente(labirinto)

while(agente.mover() != 1):
    sleep(0.3)

agente.pintarLabirinto()
