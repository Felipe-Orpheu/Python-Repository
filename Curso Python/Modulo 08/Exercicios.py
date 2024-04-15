# Exercicio 1

"""
Exercicio 1.a:
n_x = 0
n_y = 0

def num_return():

    if n_x > n_y:
        return n_x
    elif n_x < n_y:
        return n_y

print(f"O maior numero é {num_return()}")
"""


"""
Exercicio 1.b:

n_x = int(input("Escreva um numero para somar: "))
n_y = int(input("Escreva outro numero para somar: "))

def num_return():
    n_z = n_x + n_y
    return n_z

print(f"O resultado de {n_x} + {n_y} é igual a {num_return()}")
"""

# Calculadora 

print("-"*30, "Calculadora", "-"*30)

operacao = input("Por favor escolha o que ira fazer (+, -, *, /): ")
n1 = int(input("Digite um numero para calcular: "))
n2 = int(input("Digite outro numero para calcular: "))

if operacao == '+': 
    print(f'{n1} + {n2}')
    print(n1 + n2)
elif operacao == '-': 
    print(f'{n1} - {n2}')
    print(n1 - n2)
elif operacao == '*': 
    print(f'{n1} * {n2}')
    print(n1 * n2)
elif operacao == '/': 
    print(f'{n1} / {n2}')
    print(n1 / n2)
else: 
    print("Oh seu animal, como q tu deu erro em uma calculadora, explica pra mim?")
