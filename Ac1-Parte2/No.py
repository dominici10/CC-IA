from Mapa import *
import math

class No:
    '''
    Essa classe representa um noh na arvore de busca
    '''
    
    def __init__(self, estado,noPai):
        """
        Construtor
        """
        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        #self.pai= None
        self.colocaPai(noPai)
        self.fringe = True
        self.heuristica = 0
        self.calculaHeuristica()
               
    def colocaPai(self, noPai):
        """
        Esse metodo adiciona um noh em outro noh
        """
        if noPai != None:
            noPai.filhos.append(self)
            self.pai = noPai
            self.profundidade = noPai.profundidade + 1
        else:
            self.pai = None

    def addFilho(self, noFilho):
        """
        Este método adiciona um nó em outro nó
        """
        self.filhos.append(noFilho)
        noFilho.pai = self   # o noFilho aponta para o nó atual
        noFilho.profundidade = self.profundidade + 1
           
    def printArvore(self):
        """
        Este metodo faz um print da arvore de busca 
        """
        print (self.profundidade , " - " , self.estado.lugar)
        for filho in self.filhos:
            filho.printArvore()
                       
    def printCaminho(self):
        """
        Este metdo faz um print do estado inicial ateh o estado meta
        """
        if self.pai != None:
            self.pai.printCaminho()
        print ("-> ", self.estado.lugar)
        
        
    def calculaHeuristica(self):
        """
        Essa funcao calcula o valor da heuristica para esse noh
        """
        #calcula a distancia do estado atual para o estado meta
        
        #Localizacao destino
        localizacaoMeta = localizacao["Impacta"]
        #current location
        localizacaoAtual = localizacao[self.estado.lugar]
        #delta na coordenada x
        dx = localizacaoMeta[0] - localizacaoAtual[0]
        #delta na coordenada y
        dy = localizacaoMeta[1] - localizacaoAtual[1]
        #distancia
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        print ("Heuristica para ", self.estado.lugar, "=", distancia)
        self.heuristica = distancia