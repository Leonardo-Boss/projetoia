import csv 

class Labirinto:
    """
        Classe que recebe um arquivo CSV que serve para um labirinto nxm.
        O valor "-1" indica obstaculos.
        O valor "*" indica agente.
        O valor "0" indica uma posicao vazia.
        Valores diferentes indicam o valor de uma energia.
        Ex: [
            [-1,0,-1,0,0]
            [0,0,0,0,0]
            [0,-1,-1,0,0]
            [0,0,0,-1,0]
            [0,-1,0,0,0]
            [0,0,0,-1,0]
            [0,0,0,0,0]
            [0,0,-1,0,-1]
            ]
    """
    matriz = []
    
    #Metodo definido pelo desenvolvedor: @giovannilucasmoura (https://github.com/giovannilucasmoura/Labirinto-em-Grafo)
    def __init__(self, nomeArquivo):
        matriz = []
        elementos = []
        with open(nomeArquivo) as arquivo:
            leitor = csv.reader(arquivo, delimiter=',')
            for linha in leitor:
                elementos = []
                for elemento in linha:
                    elementos.append(int(elemento))
                matriz.append(elementos)
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

        