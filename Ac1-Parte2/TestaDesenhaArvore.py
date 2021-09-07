import pydot 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

EXPLORADO = "#00ee11"
ATUAL = "#ff0000"
INEXPLORADO = "#3399ff"

#cria um objeto grafo
grafo = pydot.Dot(graph_type='graph', dpi = 500)

#cria e adiciona o noh raiz
nohRaiz = pydot.Node("0-Camon Viana", style="filled", fillcolor = EXPLORADO, xlabel = "6.0")
grafo.add_node(nohRaiz)



#cria e adiciona novo noh
nohFilho1 = pydot.Node("1-Brás", style="filled", fillcolor = EXPLORADO, xlabel = "5.0")
grafo.add_node(nohFilho1)
#cria um arco entre os nos
arco1 = pydot.Edge(nohRaiz, nohFilho1)
grafo.add_edge(arco1)


#cria e adiciona novo noh
nohFilho2 = pydot.Node("2-Engenheiro Goulart", style="filled", fillcolor = INEXPLORADO, xlabel = "6.0")
grafo.add_node(nohFilho2)
#cria um arco entre os nos
arco2 = pydot.Edge(nohRaiz, nohFilho2)
grafo.add_edge(arco2)

#cria e adiciona novo noh
nohFilho3 = pydot.Node("3-Luz", style="filled", fillcolor = EXPLORADO, xlabel = "7.75")
grafo.add_node(nohFilho3)
#cria um arco entre os nos
arco3 = pydot.Edge(nohFilho1, nohFilho3)
grafo.add_edge(arco3)


#cria e adiciona novo noh
nohFilho4 = pydot.Node("4-Tatuapé", style="filled", fillcolor = INEXPLORADO, xlabel = "3.0")
grafo.add_node(nohFilho4)
#cria um arco entre os nos
arco4 = pydot.Edge(nohFilho2, nohFilho4)
grafo.add_edge(arco4)

#cria e adiciona novo noh
nohFilho5 = pydot.Node("5-Barra Funda", style="filled", fillcolor = EXPLORADO, xlabel = "4.5")
grafo.add_node(nohFilho5)
#cria um arco entre os nos
arco5 = pydot.Edge(nohFilho3, nohFilho5)
grafo.add_edge(arco5)

#cria e adiciona novo noh
nohFilho6 = pydot.Node("6-Sé", style="filled", fillcolor = INEXPLORADO, xlabel = "6.0")
grafo.add_node(nohFilho6)
#cria um arco entre os nos
arco6 = pydot.Edge(nohFilho4, nohFilho6)
grafo.add_edge(arco6)

#cria e adiciona novo noh
nohFilho7 = pydot.Node("7-Republica", style="filled", fillcolor = INEXPLORADO, xlabel = "4.5")
grafo.add_node(nohFilho7)
#cria um arco entre os nos
arco7 = pydot.Edge(nohFilho6, nohFilho7)
grafo.add_edge(arco7)

#cria e adiciona novo noh
nohFilho8 = pydot.Node("8-Pinheiros", style="filled", fillcolor = INEXPLORADO, xlabel = "4.0")
grafo.add_node(nohFilho8)
#cria um arco entre os nos
arco8 = pydot.Edge(nohFilho7, nohFilho8)
grafo.add_edge(arco8)

#cria e adiciona novo noh
nohFilho9 = pydot.Node("9-Presidente Altino", style="filled", fillcolor = INEXPLORADO, xlabel = "4.0")
grafo.add_node(nohFilho9)
#cria um arco entre os nos
arco9 = pydot.Edge(nohFilho8, nohFilho9)
grafo.add_edge(arco9)

#cria e adiciona novo noh
nohFilho10 = pydot.Node("5-Barra Funda", style="filled", fillcolor = EXPLORADO, xlabel = "4.0")
grafo.add_node(nohFilho10)
#cria um arco entre os nos
arco10 = pydot.Edge(nohFilho9, nohFilho10)
grafo.add_edge(arco10)

#cria e adiciona novo noh
nohFilho11 = pydot.Node("11-Impacta", style="filled", fillcolor = ATUAL, xlabel = "3.0")
grafo.add_node(nohFilho11)
#cria um arco entre os nos
arco11 = pydot.Edge(nohFilho5, nohFilho11)
grafo.add_edge(arco11)


#'''
#mostra o diagrama
grafo.write_png('grafo.png')
img=mpimg.imread('grafo.png')
plt.imshow(img)
plt.axis('off')
mng = plt.get_current_fig_manager()
mng.window.state('normal')
plt.show()




