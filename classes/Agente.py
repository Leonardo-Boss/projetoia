from classes.Labirinto import Labirinto

class Agente:

  nosAbertos = []
  nosFechados = []

  def __init__(self, labirinto : Labirinto, energiaInicial : int):
    self.labirinto = labirinto
    self.estadoAtual = {"coordenada": self.labirinto.agente, "energia": energiaInicial}

  #Acões
  def mover(self):
    listaRecompensas = self.labirinto.recompensas
    # Definir qual energia irei me mover
      # custoDeCaminho baixo
      # ganhoEnergetico alto
      # Executar buscaEmAmplitude para saber pontos passiveis de movimentacao  
      # labirinto.consumirEnergia(coordenada x,y)
    #Com base na lista, implementa A*
    
    pass
  #Algoritmo
