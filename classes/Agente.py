from math import fabs

class Agente:


  def __init__(self, labirinto):
    self.labirinto = labirinto
    self.coordenadaAgente = self.labirinto.agente_posicoes
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
      self.pintarLabirinto()
      self.salvar_mover()
      return 1
      
    self.getCelulasAdjacentes()
    
    celulaExpansao = max(self.abertos, key=lambda celula: celula.f_avaliacao)
    self.fechados.add(celulaExpansao)
    self.abertos.discard(celulaExpansao)

    self.coordenadaAgente = [celulaExpansao.y, celulaExpansao.x]
    if celulaExpansao.tipo == 'r':
      celula = [item for item in self.labirinto.recompensas if item[0] == celulaExpansao.y and item[1] == celulaExpansao.x][0]
      self.labirinto.recompensas.remove(celula)
      self.__caminhoFinal(celulaExpansao)
      for aberto in self.abertos:
        aberto.cost = float('inf')
        aberto.pai = None
      for fechado in self.fechados:
        fechado.cost = float('inf')
        fechado.pai = None
      self.abertos = set()
      self.fechados = set()
      self.celulaAgente = celulaExpansao
      self.celulaAgente.cost = 0
      self.fechados.add(self.celulaAgente)
      self.celulaAgente.tipo = '0'
      return 0
    self.celulaAgente = celulaExpansao
    self.pintarLabirinto()
    self.salvar_mover()

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
    


  def __abrirCelula(self, celulaExpansao):
    """
      Aqui eh feito o calculo da funcao heuristica para cada um dos alvos
    """
    if celulaExpansao.tipo != '1' and celulaExpansao.cost > self.celulaAgente.cost:

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

  def __caminhoFinal(self, celula):
    pai = celula.pai
    if pai:
      self.__caminhoFinal(pai)
    self.caminho.append(celula)

  def __str__(self):
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

    return f"{str_lab}\n"

  def pintarLabirinto(self):
    print(self)
    print(self.labirinto.seed)



  def salvar_mover(self):
    
    def lista(lista):
      string = ''
      for item in lista:
        string = f'{string}({item.x}, {item.y}), '
      string = f'{string}]\n'
      return string

    string = str(self)
    
    string = f'{string}abertos: ['
    string = f'{string}{lista(self.abertos)}'
    string = f'{string}fechados: ['
    string = f'{string}{lista(self.fechados)}'
    
    with open(f'{self.labirinto.seed}.txt', 'a') as f:
      f.write(string)

  def salvar_header(self):
    string = ''
    def lista(lista):
      string = ''
      for item in lista:
        string = f'{string}(valor: {item[2]}, x: {item[1]}, y:{item[0]}), '
      string = f'{string}]\n'
      return string
    string = f'{string}seed: {self.labirinto.seed}\n'
    string = f'{string}recompensas: ['
    string = f'{string}{lista(self.labirinto.recompensas)}'
    string = f'{string}agente: [x: {self.labirinto.agente_posicoes[1]}, y: {self.labirinto.agente_posicoes[0]}]\n'
    with open(f'{self.labirinto.seed}.txt', 'a') as f:
      f.write(string)