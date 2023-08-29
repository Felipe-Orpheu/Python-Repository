lista = ["chicago", "queens", "salvador", "pernanbuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 2.5, 6.3]
print(lista3)

lista2 = lista2 + lista3
print(lista2)

lista4 = [True, False]
print(lista4)

#index      0      1        2     3    4  5 -> 6 elemetos
lista5 = [True, "Chicago", 2.5, False, 4, 8]
print(lista5)

print(type(lista5))

# Slicing - OBS: funciona com strings tbm!!!

print(lista5[1:]) # retorna do index desejado até o fim da lista
print(lista5[2:]) # retorna do index desejado até o fim da lista
print(lista5[:3]) # retorna index 0 até o desejado
print(lista5[:4]) # retorna index 0 até o desejado
print(lista5[1:4]) # retorna do index destacado até o valor que desejamos mostrar
print(lista5[1:5:2])
    