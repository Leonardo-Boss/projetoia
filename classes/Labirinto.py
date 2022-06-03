from random import randint

class Celula:
    def __init__(self, tipo):
        self.tipo = tipo
        self.cost = float('inf')    # o custo deve ser infinito inicialmente porque o custo apenas é trocado quando um custo menor é encontrado
        self.manhattan = []         # lista com distancias manhattan até cada um dos objetivos
        self.pai = None             # célula anterior no caminho, para tracejar a rota

class Labirinto:
    """
        # Classe que recebe um arquivo BPM que representa um labirinto.

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
    
    def __init__(self, path, seed=None):
        matriz = self.__pbm_to_matrix(path)

        self.labirinto = {l: {s: Celula(matriz[l][s]) for s in range(len(matriz[l]))} for l in range(len(matriz))}

        # self.recompensas, self.agente = self.__setRecompensas(seed) metodo __setRecompensas ainda precisa ser implementado

    def __getCelulasVazias(self):
        """
        Metodo que captura todas as posicoes em branco do tabuleiro, passiveis de posicionamento.
        :return list celulasVazias
        """
        return [cell for line in self.labirinto.values() for cell in line.values() if cell.tipo == '0']

    def __getPosicoes(self):

        """
            Metodo que deve retornar uma tupla com posições e valores para alvos e posição do agente
            exemplo:
            
                (
                    [
                        [x, y, valor],
                        [x, y, valor],     # lista com posição e valores para os alvos
                        [x, y, valor],
                    ],
                    [x,y]                       # lista com posição para o agente
                )
        """

        """
            Deve considerar posições em branco com o metodo getCelulasVazias
            Deve considerar que o agente nao pode ser gerado em um obstaculo ou em um alvo
            Aqui será implementada a logica que definirá onde serão spawnadas os alvos e o agente
        """

        voidList = self.__getCelulasVazias(); #[[0,0],[0,1],[1,1],[5,7],[20,20],[10,10]] 
        posicoes = [] 

        for i in range(3): #define valores e posições dos alvos
            c = randint(0,(len(voidList)-1))
            aux = voidList[c]
            aux.append(randint(1,50))
            posicoes.append(aux)
            voidList.pop(c)

        c = randint(0,(len(voidList)-1)) #define posição do agente
        posicoes.append(voidList[c])
        voidList.pop(c)

        posicoes = tuple(posicoes)

        return posicoes
              

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

    def __pbm_to_matrix(self, pbm):
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
