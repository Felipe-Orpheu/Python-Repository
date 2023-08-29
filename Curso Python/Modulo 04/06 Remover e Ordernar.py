#index       0       1        2
lista = ["carro", "barco", "avião"]
print(lista)

#lista.pop(0) #serve igual a função append, mas para remover elementos.
#lista.remove("barco") #remove o valor especifico.
#del lista - para deletar a lista enteira.
#del lista[0] - para deletar um valor expecifico dentro da lista.    

"""carrinho_de_compras = ["pão", "carne", "verduras", "alface"]
carrinho_de_compras.clear #apaga todos os elementos, mas nao o index em si.
carrinho_de_compras.sort() #ordenação em ordem crescente"""

"""
lista = [1, 50, 23, 67, 100]
print(lista)

lista.sort(reverse = True) #ordenação em ordem decrescente
lista.reverse() 
print(lista)
"""

lista = ["Ana", "Pedro", "Marta", "Clarice", "beatriz", "ana clara"]
print(lista)

lista.sort(key = str.lower) #para ordenar a lista mesmo com que tenha os valores minusculos e maiusculos juntos.
print(lista)