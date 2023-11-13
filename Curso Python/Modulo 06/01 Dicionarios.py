#Listas: Coleção Ordenada, mutavel e que permite valores duplicados
#Tuplas: Coleção ordenada, imutavel e que permite valores duplicados
#Dicionarios: Coleção nao ordenada, mutavel e que não permite valores duplicados

#index     0         1
lista = ["item1", "item2"]
tuplas = ("item1", "item2")

#dicionario: chave:valor
dicio = {"chave1" : "Gabriel", "chave2" : 1993, "chave3" : True}
print(dicio)

dicionario = {
    "nome": "Bruna", 
    "idade": 27, 
    "nascionalidade": "Brasileira",
    "idade": 35
}
print(dicionario)
print(dicionario["idade"])

print(dicionario.get("idade"))

print(dicionario.keys()) #mostra todas as chaves do dicionario
print(len(dicionario)) #mostra quantos elementos existem no dicionario
print(dicionario.values()) #mosta os valores dentro de um dicionario

if "idade" in dicionario: 
    print("A chave idade existe!")

print(dicionario.items())