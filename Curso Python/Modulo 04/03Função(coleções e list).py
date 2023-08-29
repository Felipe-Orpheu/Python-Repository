lista1 = [2.0, 3.5, 4.7]
print(lista1)

lista2 = [1, 5, 9, 11, 15]
print(lista2)

lista3 = ["nome", "nome2", "nome"] #Uma lista sempre ultiliza o index para saber os parametros da lista
print(len(lista3))

print(len(lista1)) #para saber o tamanho da lista registrada.
print(len(lista2))

#Funções que só podem ser ultilizado com tipos de dados numericos

print(sum(lista1)) #Soma os valores da lista
print(max(lista2)) #Saber o maior valor da lista
print(min(lista2)) #Mosta o valor minimo da lista 

#----------------------------------------------------------------------------------#

nome = "Cuso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list("Cuso de Python")
print(lista8)

elemento = 8

if elemento in lista7: 
    print("Este elemento esta dentro da lista")