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

        self.labirinto = {l: {c: Celula(matriz[l][c]) for c in range(len(matriz[l]))} for l in range(len(matriz))}

        # self.recompensas, self.agente = self.__getPosicoes(seed) metodo __setRecompensas ainda precisa ser implementado

    def __getCelulasVazias(self):
        """
        Metodo que captura todas as posicoes em branco do tabuleiro, passiveis de posicionamento.
        :return list celulasVazias
        """
        return [cell for line in self.labirinto.values() for cell in line.values() if cell.tipo == '0']
              
    def __setRecompensas(self, seed):
        """
            Metodo que recebe uma seed e deve retornar uma tupla com posições e valores para premios/energias e agente
            exemplo:
            
                (
                    [
                        {'valor': int, 'x': int, 'y': int},
                        {'valor': int, 'x': int, 'y': int},     # lista com posição e valores para os premios/energias
                        {'valor': int, 'x': int, 'y': int}
                    ],
                    {'x': int, 'y': int}                        # dicionario com posição para o agente
                )
        """

        """
            Deve considerar posições em branco com o metodo getCelulasVazias
            Deve considerar que o agente nao pode ser gerado em um obstaculo ou em um alvo
            Aqui será implementada a logica que definirá onde serão spawnadas as energias e o agente
        """
        
        celulasVazias = self.__getCelulasVazias()

        pass
    
    def __str__(self):
        string = ''
        for linha in self.labirinto:
            for celula in linha:
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
