from Mapa import *

class Estado:
    
    def __init__(self, lugar = None):
        if lugar== None:
            #create initial state
            self.lugar = self.pegaEstadoInicial()
        else:
            self.lugar = lugar
    
    def pegaEstadoInicial(self):
        """
        Este metodo retorna o estado incial da busca
        """
        estadoInicial= "Camon Viana"
        return estadoInicial

    def funcaoSucessora(self):
        """
        Esta é a função sucessora. Gera todo os possiveis
        lugares que podem ser alcançados a partir do estado atual.
        """
        return conexoes[self.lugar]        
        
    def funcaoObjetivo(self):
        """
        Este método verifica se o caminho está no estado objetivo
        """
        #verifica que o lugar atual eh o carregamento
        return self.lugar == "Impacta"


        




