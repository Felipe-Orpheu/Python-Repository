#Paradigma imperativo
#O que mais usamos foi o paradigma imperativo 

#caracteristicas de um paradigma imperativo: variáveis, atribuições e sequência
#Linguagens que ultilizão este paradigma: C, Fortran, Kobol, Basic, Pascal, Ada, Modula-2

#bloco externo
nome = "Gabriel" #variavel global


def minha_funcao():
    #bloco interno *bloco interno de uma função é conhecido como corpo da função
    nome = "Ana" #variavel local
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno da condição if")
    for x in tupla: 
        print(x)
    

print(nome)
minha_funcao()