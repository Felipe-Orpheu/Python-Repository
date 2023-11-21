"""
Paradigma Imperativo

SUAS CARACTERISTICAS:
variaveis, atribuições e principalmente sequência

Linguagens de ultilizam paradigmas imperativos:
C, Fortran, Kobol, Basic, Pascal, Ada, Modula-2
"""

#bloco externo
nome = "Gabriel" #variavel global

def minha_funcao():
    #Bloco interno *bloco interno de uma função é cinhecido como corpo da função

    nome = "Ana" #Variavel local
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno da condição if")
    for x in tupla:
        print(x)


minha_funcao()
print(nome)
