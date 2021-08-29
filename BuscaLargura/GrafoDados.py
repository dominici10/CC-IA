#criar um dicionário com todos os mapeamentos
conexoes = {}
conexoes ["Camon Viana"] = {"Brás", "Engenheiro Goulart"}
conexoes ["Brás"] = {"Luz", "Camon Viana"}
conexoes ["Luz"] = {"Brás", "Barra Funda"}
conexoes ["Engenheiro Goulart"] = {"Tatuapé","Camon Viana"}
conexoes ["Tatuapé"] = {"Sé","Engenheiro Goulart"}
conexoes ["Sé"] = {"Barra Funda", "Republica","Tatuapé"}
conexoes ["Republica"] = {"Pinheiros","Sé"}
conexoes ["Pinheiros"] = {"Presidente Altino","Republica"}
conexoes ["Presidente Altino"] = {"Barra Funda","Pinheiros"}
conexoes ["Barra Funda"] = {"Impacta","Sé","Presidente Altino","Luz"}
conexoes ["Impacta"] = {"Barra Funda"}
