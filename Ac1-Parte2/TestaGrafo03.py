from No import No
from Estado import Estado
from DesenhaArvore import DesenhaArvore

estadoInicial = Estado()
estadoAtual = Estado("Camon Viana")
raiz = No(estadoInicial,None)
raiz.fringe = False
noAtual = No(estadoAtual,None)

estadosFilhos = estadoInicial.funcaoSucessora()
for estadoFilho in estadosFilhos:
    noFilho = No(Estado(estadoFilho),raiz)
    estadosNetos = Estado(estadoFilho).funcaoSucessora()
    for estadoNeto in estadosNetos:
        estadoNeto = No(Estado(estadoNeto),noFilho)


plotaArvore = DesenhaArvore()
plotaArvore.criaDiagrama(raiz,noAtual)







