"""
#         chave :  valor
dicio = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
print(dicio)

#Formas simples de modificar um ou mais valores na chave
dicio["nome"] = "Pedro" 
print(dicio)

dicio.update({"nome": "Ana"})
print(dicio)

dicio["idade"] = 32 #Isto acrescentou mais uma chave ao dicionario 
print(dicio)

dicio.update({"estado":"Rio de Janeiro"})
print(dicio)
"""

dados = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
dados.update({"estado":"Rio de Janeiro"})
print(dados)

dados.popitem() #Elimina o ultimo item do dicionario 
print(dados)

dados.pop("valor_logico") #apaga o item selecionado
print(dados)

del dados["ano"] #tbm apaga o item selecionado
print(dados)

dados.clear() #apaga todos os itens do dicionario
print(dados)

#loop com dicionario
dados = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
dados.update({"estado":"Rio de Janeiro"})

dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)

dados["idade"] = 27
print(dados)
print(dicio)
print(dicio2)

