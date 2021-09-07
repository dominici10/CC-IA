#conexoes entre pontos
conexoes = {}
conexoes ["Camon Viana"] = {"Brás", "Engenheiro Goulart"}
conexoes ["Brás"] = {"Luz"}
conexoes ["Luz"] = {"Brás", "Barra Funda"}
conexoes ["Engenheiro Goulart"] = {"Tatuapé"}
conexoes ["Tatuapé"] = {"Sé","Engenheiro Goulart"}
conexoes ["Sé"] = {"Barra Funda", "Republica","Tatuapé"}
conexoes ["Republica"] = {"Pinheiros","Sé"}
conexoes ["Pinheiros"] = {"Presidente Altino","Republica"}
conexoes ["Presidente Altino"] = {"Barra Funda","Pinheiros"}
conexoes ["Barra Funda"] = {"Impacta","Sé","Presidente Altino","Luz"}
conexoes ["Impacta"] = {"Barra Funda"}
#conexoes["Estacao 4"] = {"Home e Energia", "Estoque Pronto"}

#localização de todos os lugares 

localizacao = {}
localizacao["Camon Viana"] = [14, 8]
localizacao["Brás"] = [13, 7]
localizacao["Luz"] = [12, 5]

localizacao["Engenheiro Goulart"] = [12, 8]
localizacao["Tatuapé"] = [4, 10]

localizacao["Sé"] = [6, 8]

localizacao["Republica"] = [7, 5]
localizacao["Pinheiros"] = [4, 4]
localizacao["Presidente Altino"] = [5, 2]
localizacao["Barra Funda"] = [8, 3]
localizacao["Impacta"] = [8, 0]