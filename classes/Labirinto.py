import csv 

class Labirinto:
    """
        #Classe que recebe um arquivo BPM que representa um labirinto.

        O valor "1" indica obstaculos.

        O valor "0" indica uma posicao vazia.

        Ex: [
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                ['1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'],
                ['1', '0', '1', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '0', '1'],
                ['1', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1'],
                ['1', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
                ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1'],
                ['1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'],
                ['1', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1'],
                ['1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
                ['1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1'],
                ['1', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1'],
                ['1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1'],
                ['1', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
                ['1', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1'],
                ['1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '1', '0', '1'],
                ['1', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
                ['1', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '0', '1'],
                ['1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '1'],
                ['1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ]
    """
    matriz = []
    
    def __init__(self, nomeArquivo):
        matriz = self.__pbm_to_matrix(nomeArquivo)
        
        self.matriz = matriz

    def getCelulasVazias(self):
        """
        Metodo que captura todas as posicoes em branco do tabuleiro, passiveis de posicionamento.
        :return list celulasVazias
        """
        pass
              
    def setPosicoes(self, energiaAlvos : list[int]):
        """
            Metodo que recebe uma lista de energias (alvos) e as posiciona, assim como o agente.
        """

        """
            Deve considerar posições em branco com o metodo getCelulasVazias
            Deve considerar que o agente nao pode ser gerado em um obstaculo ou em um alvo
            Aqui será implementada a logica que definirá onde serão spawnadas as energias e o agente
        """
        
        celulasVazias = self.getCelulasVazias()
        # Ex:
        # [-1 , * , -1]
        # [23 , 0 , -1]
        # [-1 , 34, -1]
        pass

    def getPosicaoAgente():
        # Retorna a posição inicial do agente;
        # Ex : [2,2]
        return 0;

    def getPosicaoEnergiaAlvo():
        # Retornar uma lista de dicionarios
        # [
        # {"coordenada": [x,y], "energia": int},
        # {"coordenada": [x,y], "energia": int}
        # ]
        return 0;

    def __pbm_to_matrix(pbm):
        """
            recebe path para arquivo pbm, o arquivo deve seguir o seguinte formato:

            p1\n
            \# comentario\n
            (largura) (altura)\n
            101010101011...\n
        """
        with open(pbm, 'r') as f:
            lines = f.read()
        lines = lines.split('\n')
        x, y = lines[2].split(' ')
        body = ''.join(lines[3:])
        matrix = []
        i = 0
        for _ in range(int(y)):
            line = []
            for _ in range(int(x)):
                line.append(body[i])
                i += 1
            matrix.append(line)
        return matrix

class Celula:
    def __init__(self, tipo):
        self.tipo = tipo
        self.cost = float('inf')    # o custo deve ser infinito inicialmente porque o custo apenas é trocado quando um custo menor é encontrado
        self.manhattan = []         # lista com distancias manhattan até cada um dos objetivos
        # self.prioridade = []      # melhor implementar no agente, será uma lista com o valor de cada objetivo então será igual para todas as células
        self.pai = None             # célula anterior no caminho, para tracejar a rota

    # def avaliação(self):              # faz mais sentido implementar no agente
    #     pass