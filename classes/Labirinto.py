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

    def __str__(self):
        return f'({self.x}, {self.y})'

class Labirinto:

    matriz = []

    def __init__(self, path, seed_value=randint(0,1000)):
        self.seed = seed_value
        seed((seed_value))

        """
        # A variavel matriz recebe através do método __pbm_to_matrix um arquivo PBM que representa um labirinto.
        O valor "1" indica obstaculos.
        O valor "0" indica uma posicao vazia.
        """
        matriz = self.__pbm_to_matrix(path)

        """
        Utiliza a matriz que é recebida pelo csv e itera para criar um dicionario de de objetos (do tipo Celula) que
        que pode ser acessado através da linha e coluna;
        """

        self.labirinto = {l: {c: Celula(matriz[l][c], l, c) for c in range(len(matriz[l]))} for l in range(len(matriz))}

        self.celulas_vazias = self.__getCelulasVazias()

        self.recompensas, self.agente_posicoes = self.__getPosicoes()

        self.labirinto[self.agente_posicoes[0]][self.agente_posicoes[1]].cost = 0
        
        #([16, 4, 49], [16, 11, 21], [14, 5, 42], [16, 8])
        for recompensa in self.recompensas:
            self.labirinto[recompensa[0]][recompensa[1]].tipo = 'r'
        

    def __getCelulasVazias(self):
        """
        Metodo que captura todas as posicoes em branco do tabuleiro, passiveis de posicionamento.
        """
        return [[l, c] for l, line in self.labirinto.items() for c, cell in line.items() if cell.tipo == '0']

    def __getPosicoes(self):
        'Metodo que retorna uma tupla com posições e valores para alvos e posição do agente'
        voidList = deepcopy(self.celulas_vazias);
        posicoes = [] 
        for i in range(3): #define valores e posições dos alvos
            c = randint(0,(len(voidList)-1))
            aux = voidList[c] # aux = [x,y]
            aux.append(randint(50,100)) #aux = [x,y,valor]
            posicoes.append(aux)
            voidList.pop(c)

        c = randint(0,(len(voidList)-1)) #define posição do agente
        posicoes = (posicoes, voidList[c])
        
        return posicoes
    
    def list_str(self):
        string = []
        for linha in self.labirinto.values():
            linhas = []
            for celula in linha.values():
                match celula.tipo:
                    case '0':
                        linhas.append('⬜\u200c')
                    case '1':
                        linhas.append('⬛\u200c')
                    case 'r':
                        linhas.append('🟨\u200c')
            string.append(linhas)
        return string

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
                    # case 'a':
                    #     string = f'{string}🟥\u200c'
                    # case 'f':
                    #     string = f'{string}🟩\u200c'
                    # case 'ab':
                    #     string = f'{string}🟦\u200c'
                    # case 'c':
                    #     string = f'{string}🟪\u200c'
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
