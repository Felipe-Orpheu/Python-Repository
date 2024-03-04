"""
def imprimir_nome(nome, sobrenome, idade):
    print("nome: ", nome)
    print("sobrenome: ", sobrenome)
    print("idade: ", idade)


sobrenome = "clara"
idade = 35
imprimir_nome(sobrenome=sobrenome, idade=idade, nome="maria")
"""





"""
#Parametro Padrão - Define argumentos não obrigatorios
def imprimir_nome(nomeImovel, n_quartos, vagasGaragem = None, ):
    print("------------")
    print("Titulos: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)


#Exemplos de n° de argumentos <= n° dos parâmetros
print()
imprimir_nome("Casa 3 Quartos - SP", 3)
imprimir_nome("Apartamento - NG", 2, 1)

#Exemplos de n° de argumentos > n° dos parametos
#imprimir_nome("Loja Comercial", 2, 5, "desconto")
"""


#Argumento arbitrario *args - Essa função recebe argumentos q serão atribuidos em uma tupla

"""def imprimir_nome(nomeImovel, n_quartos, vagasGaragem = None, *telefones):
    print("------------")
    print("Titulos: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)
    print("telefones: ", telefones)


imprimir_nome("Loja Comercial", 2, 5, "61 5555-55555", "21 5555-5555")"""

"""def imprimir_nomes(*nomes):
    print(nomes[0])
    print(type(nomes))

lista = ["ana", "beatris", "pedro", "joao"]
imprimir_nomes(*lista)"""

# Argumentos Arbitrarios **Kwargs - Keyword Arguments
# Essa função recebe argumentos que serão atribuidos em um dicionario

"""def imprimir_nomes(**nomes): 
    print(f"{nomes['nome']} {nomes['sobrenome']}")


dicio = {'nome': 'ana', 'sobrenome:': 'julia'}
imprimir_nomes(dicio)"""