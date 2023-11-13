tupla = "item1", "item2", "item3", "item4"
lista = list(tupla) #Transformar um tupla em uma lista
print(tupla)
print(lista)

lista.append("item5") #Adicionar itens na lista
print(lista)

tupla = tuple(lista) #Transformar uma lista em tupla
print(tupla)

lista.pop() #Apagar o item da lista
print(lista)

del tupla #Apaga a tupla
print(tupla)
