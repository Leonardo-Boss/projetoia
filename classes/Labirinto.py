from random import randint, seed
from copy import deepcopy

class Celula:      #tipo eh o valor 1 ou 0
    def __init__(self, tipo, y, x):
        self.tipo = tipo
        self.cost = float('inf')    # o custo deve ser infinito inicialmente porque o custo apenas é trocado quando um custo menor é encontrado
        self.manhattan = [None, None, None]         # lista com distancias manhattan até cada um dos objetivos
        self.pai = None             # célula anterior no caminho, para tracejar a rota
        self.f_avaliacao = None
        self.x = x
        self.y = y

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

    def __init__(self, path, seed_value=None):
        seed(seed_value)

        matriz = self.__pbm_to_matrix(path)
        """
            labirinto = {}
            for l in range(len(matriz)):
                for c in range(len(matriz[l]))
                    labirinto[l] = {c: Celula(matriz[l][c])}
        """
          #pega o tamanho da matriz ai vai interar
        self.labirinto = {l: {c: Celula(matriz[l][c], l, c) for c in range(len(matriz[l]))} for l in range(len(matriz))}

        self.celulas_vazias = self.__getCelulasVazias()

        self.recompensas, self.agente_posicoes = self.__getPosicoes()

        self.labirinto[self.agente_posicoes[0]][self.agente_posicoes[1]].cost = 0
        
        #([16, 4, 49], [16, 11, 21], [14, 5, 42], [16, 8])
        for recompensa in self.recompensas:
            self.labirinto[recompensa[0]][recompensa[1]].tipo = 'r'
        
        self.labirinto[self.agente_posicoes[0]][self.agente_posicoes[1]].tipo = 'a'

    def __getCelulasVazias(self):
        """
        Metodo que captura todas as posicoes em branco do tabuleiro, passiveis de posicionamento.
        :return list celulasVazias
        """
        return [[l, c] for l, line in self.labirinto.items() for c, cell in line.items() if cell.tipo == '0']

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
        voidList = deepcopy(self.celulas_vazias); #[[1,2],[2,2],[2,3],[3,1],[4,2],[1,1]] 
        posicoes = [] 
        for i in range(3): #define valores e posições dos alvos
            c = randint(0,(len(voidList)-1))
            aux = voidList[c] # aux = [x,y]
            
            aux.append(randint(1,50)) #aux = [x,y,valor]
            posicoes.append(aux)
            voidList.pop(c)

        c = randint(0,(len(voidList)-1)) #define posição do agente
        posicoes = (posicoes, voidList[c])
        
        return posicoes
    
    def __str__(self):
        string = ''
        for linha in self.labirinto.values():
            for celula in linha.values():
                match celula.tipo:
                    case '0':
                        string = f'{string}⬜\u200c'
                    case '1':
                        string = f'{string}⬛\u200c'
                    case 'r':
                        string = f'{string}🟨\u200c'
                    case 'a':
                        string = f'{string}🟥\u200c'
            string = f'{string}\n'
        return string

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
