#index      0       1        2
lista = ["carro","barco", "aviao"]
print(lista)

"""lista.append("moto") - adiciona valores a lista
print(lista)"""

"""lista.insert(1, "bicicleta") - insere um valor de cada 1, sendo o valor index a mudar e o valor a ser inserido
print(lista)"""

#lista.extend(["bicicleta", "navio"]) - Insere separadamente cada valor dentro da lista

for x in range(len(lista)): 
    print(x, lista[x])

texto = "meunome@gmail.com"
lista2 = list(texto)
print(lista2)

texto = texto.split('@') #separa as categorias pelo que esta determinado
print(texto)



