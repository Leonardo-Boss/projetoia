from math import fabs
from classes.Labirinto import Labirinto, Celula

class Agente:


  def __init__(self, labirinto : Labirinto):
    self.labirinto = labirinto
    self.coordenadaAgente = labirinto.agente_posicoes
    self.celulaAgente = self.labirinto.labirinto[self.coordenadaAgente[0]][self.coordenadaAgente[1]]
    self.abertos = []
    self.fechados = []
    self.adjacentes = []

  #Acões
  def mover(self):
    # Definir qual alvo irei me mover
      # custoDeCaminho baixo
      # ganho alto
      # Executar buscaEmAmplitude para saber pontos passiveis de movimentacao  
    #Com base na lista, implementa A*

    if(self.__caminhoFinal == len(self.labirinto.recompensas)):
      return 0
      
    self.getCelulasAdjacentes()
    
    celulaExpansao = max(self.abertos, key=lambda celula: celula.f_avaliacao)
    self.fechados.append(celulaExpansao)
    self.abertos.remove(celulaExpansao)
    self.coordenadaAgente = [celulaExpansao.y, celulaExpansao.x]
    if celulaExpansao.tipo == 'r':
      celula = [item for item in self.labirinto.recompensas if item.y == celulaExpansao.y and item.x == celulaExpansao.x][0]
      self.labirinto.recompensas.pop(celula)
      
    
    celulaExpansao.tipo = 'a'
    self.celulaAgente.tipo = '0'
    self.celulaAgente = celulaExpansao

  #Algoritmo

  def getCelulasAdjacentes(self):
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
    if celulaExpansao.tipo != '1' and celulaExpansao.cost > self.celulaAgente.cost:

      self.abertos.append(celulaExpansao)
      
      if celulaExpansao in self.fechados:
        self.fechados.remove(celulaExpansao)

      celulaExpansao.pai = self.celulaAgente
      celulaExpansao.cost = self.celulaAgente.cost + 1
      f_avaliacao = []

      for i, recompensa in enumerate(self.labirinto.recompensas):
        celulaExpansao.manhattan[i] = fabs(recompensa[0]-self.coordenadaAgente[0])+fabs(recompensa[1]-self.coordenadaAgente[1])
        f_avaliacao.append(recompensa[2] - celulaExpansao.cost - celulaExpansao.manhattan[i])

      celulaExpansao.f_avaliacao =  max(f_avaliacao)

  def __caminhoFinal(self, celula):
    recompensas = 0
    pai = celula.pai
    if pai:
      recompensas += self.__caminhoFinal(pai)
    if celula.tipo == 'r':
      recompensas += 1
    return recompensas

  def encontrar(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(lista)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices

