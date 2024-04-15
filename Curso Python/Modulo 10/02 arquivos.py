"""arquivo = open('./Modulo 10/receita.txt')
print(arquivo.readline()) #Serve para ler o arquivo em TXT ou outro arquivo
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)"""

"""with open('./Modulo 10/receita.txt') as arquivo:
    print(arquivo.closed)
    print(arquivo.read())
print(arquivo.closed)"""

texto = """a
b
c
"""

with open('./Modulo 10/receita.txt', 'a') as a: 
    a.write(texto)

#'w' para poder escrever
#'a' para colocar mais de uma palavra no texto