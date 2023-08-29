lista = ["a", "b", "c"]
print(lista)

lista2 = lista.copy()
print(lista)

lista2.append("d")
lista.append("e")

print(lista)
print(lista2)
