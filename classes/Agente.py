
from classes.Labirinto import Labirinto

class Agente:

  nosAbertos = []
  nosFechados = []

  def __init__(self, labirinto : Labirinto, energiaInicial : int):
    self.labirinto = labirinto
    self.estadoAtual = {"coordenada": self.labirinto.getPosicaoAgente, "energia": energiaInicial}

  #Acões
  def mover(self):
    listaEnergia = self.labirinto.getPosicaoEnergiaAlvo()
    # Definir qual energia irei me mover
      # custoDeCaminho baixo
      # ganhoEnergetico alto
      # Executar buscaEmAmplitude para saber pontos passiveis de movimentacao  
      # labirinto.consumirEnergia(coordenada x,y)
    #Com base na lista, implementa A*
    
    pass




  def isEnergia(self):
    # Verificar se a posicao atual (coordenadas) , e correspondente ao posicionamento de uma energia
    # Metodos que devem ser utilizados : getPosicaoEnergiaAlvo()
    pass

  #Algoritmo