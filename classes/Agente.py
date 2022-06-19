from math import fabs
from random import randint
from typing import Set

from classes.Labirinto import Celula, Labirinto


class Agente:


  def __init__(self, path, seed=randint(0,1000)):
    self.seed = seed
    self.path = path
    self.labirinto = Labirinto(path, seed)
    
    #coordenadaAgente é referente a posição inicial do meu agente no labirinto.
    self.coordenadaAgente = self.labirinto.agente_posicoes
    
    #celulaAgente é referente a posição atual do agente.
    self.celulaAgente = self.labirinto.labirinto[self.coordenadaAgente[0]][self.coordenadaAgente[1]]
    
    self.abertos = set()
    self.fechados = {self.celulaAgente}
    self.caminho = []

  #Acões
  def mover(self):
    # Definir qual alvo irei me mover
      # custoDeCaminho baixo
      # ganho alto
      # Executar buscaEmAmplitude para saber pontos passiveis de movimentacao  
    #Com base na lista, implementa A*

    if(len(self.labirinto.recompensas) == 0):
      return 1
      
    self.getCelulasAdjacentes() # Adiciona ao set de abertos as celulas adjacentes ao agente
    
    celulaExpansao = max(self.abertos, key=lambda celula: celula.f_avaliacao) # Expande para a maior função avaliação
    self.fechados.add(celulaExpansao) # Adiciona ao set de fechados a celula expandida
    self.abertos.discard(celulaExpansao) # Retira do set de abertos a celula expandia

    self.coordenadaAgente = [celulaExpansao.y, celulaExpansao.x] # Sempre que se move o agente reatribui suas coordenadas na "coordenadaAgente"
    if celulaExpansao.tipo == 'r': # Se for uma recompensa
      celula = [item for item in self.labirinto.recompensas if item[0] == celulaExpansao.y and item[1] == celulaExpansao.x][0] # Atribui a celula recompensa a variavel
      self.labirinto.recompensas.remove(celula) # Remove a celula da lista de recompensas
      self.__caminhoFinal(celulaExpansao) # Executa recursão para descobrir o caminho final
      
      # Se achou uma recompensa, redefine o tabuleiro para o estado inicial 
      for aberto in self.abertos: 
        aberto.cost = float('inf')
        aberto.pai = None
      for fechado in self.fechados:
        fechado.cost = float('inf')
        fechado.pai = None
      self.abertos = set()
      self.fechados = set()
      
      #Pequenas alterações para que o jogo possa continuar da recompensa que ele acabou de pegar
      self.celulaAgente = celulaExpansao
      self.celulaAgente.cost = 0
      self.fechados.add(self.celulaAgente)
      self.celulaAgente.tipo = '0'
      return 0
      
    self.celulaAgente = celulaExpansao # Altero a celula onde o agente se encontra para a celula q foi expandida


  def getCelulasAdjacentes(self): # Adiciona ao set de abertos os nós adjacentes
    pos_y_agente, pos_x_agente = self.coordenadaAgente
    """
      Retorna as celulas adjacentes passiveis de movimentacao. O tabuleiro eh visto na perspectiva do canto inferior direito (a iteracao eh feita de cima para baixo)
    """
    
    up = self.labirinto.labirinto[pos_y_agente-1][pos_x_agente]
    self.__abrirCelula(up)

    down = self.labirinto.labirinto[pos_y_agente+1][pos_x_agente]
    self.__abrirCelula(down)

    right = self.labirinto.labirinto[pos_y_agente][pos_x_agente+1]
    self.__abrirCelula(right)
    
    left = self.labirinto.labirinto[pos_y_agente][pos_x_agente-1]
    self.__abrirCelula(left)
    


  def __abrirCelula(self, celulaExpansao:Celula):
    """
      Aqui eh feito o calculo da funcao heuristica para cada um dos alvos
    """
    if celulaExpansao.tipo != '1' and celulaExpansao.cost > self.celulaAgente.cost: # Abrir apenas celulas que não estão abertas

      self.abertos.add(celulaExpansao)
      
      if celulaExpansao in self.fechados:
        self.fechados.discard(celulaExpansao)

      celulaExpansao.pai = self.celulaAgente
      celulaExpansao.cost = self.celulaAgente.cost + 1
      f_avaliacao = []

      for i, recompensa in enumerate(self.labirinto.recompensas):
        celulaExpansao.manhattan[i] = fabs(recompensa[0]-celulaExpansao.y)+fabs(recompensa[1]-celulaExpansao.x)
        f_avaliacao.append(recompensa[2] - 0.7*celulaExpansao.cost - celulaExpansao.manhattan[i])
      celulaExpansao.f_avaliacao =  max(f_avaliacao)

      if celulaExpansao.y == 14 and celulaExpansao.x == 9:
        pass

  def __caminhoFinal(self, celula): # Função recursiva que é executada no final da execução, que basicamente entra o pai de todas as celulas de forma iterativa
    pai = celula.pai
    if pai:
      self.__caminhoFinal(pai)
    self.caminho.append(celula)

  def pintarLabirinto(self):
    str_lab = self.labirinto.list_str()
    for passo in self.caminho:
      str_lab[passo.y][passo.x] ='🟪\u200c'
    for fechado in self.fechados:
      str_lab[fechado.y][fechado.x] = '🟩\u200c'
    for aberto in self.abertos:
      str_lab[aberto.y][aberto.x] = '🟦\u200c'
    str_lab[self.coordenadaAgente[0]][self.coordenadaAgente[1]] = '🟥\u200c'
    str_str = []
    for l in str_lab:
      str_str.append(''.join(l))
    
    str_lab = '\n'.join(str_str)
    print(str_lab,'\n')
    print(self.seed)
