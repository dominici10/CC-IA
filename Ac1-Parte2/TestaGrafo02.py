from No import No
from Estado import Estado
from DesenhaArvore import DesenhaArvore

estadoInicial = Estado("Camon Viana")
raiz = No(estadoInicial,None)
raiz.fringe = False


estadosFilhos = estadoInicial.funcaoSucessora()
for estadoFilho in estadosFilhos:
    noFilho = No(Estado(estadoFilho),raiz)
    noAtual =noFilho

plotaArvore = DesenhaArvore()
plotaArvore.criaDiagrama(raiz,noAtual)







