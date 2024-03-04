
"""numeroInt = 5

def reduzirNumero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1

reduzirNumero(10)"""

"""
1- checar se o nosso numero não é igual a 0 
2- se ele não for igual a 0 - reduzir 1 unidade

5 {N - 1}
 4 (5 - 1)
  3 (4 - 1)
   2 (3 - 1)
    1 (2 - 1)
     0 (1 - 1)
"""

"""def reduzirNumero(numeroInt):
    print(numeroInt)
    if numeroInt > 0:
        # N - 1
        reduzirNumero(numeroInt - 1)
        print(numeroInt)

reduzirNumero(5)"""


# Fatorial - Sem Recurção
def fatorialS(numero):
    fatorial = 1 
    if numero == 0: 
        return 1 
    else: 
        for x in range(1, numero + 1): 
            fatorial *= x
        return fatorial

print(fatorialS(5))


# Fatorial - Solução Recursiva
def fatorialR(numero): 
    if numero == 0: # Criterio de Parada
        return 1 
    else: 
        return numero * fatorialR(numero - 1)

print(fatorialR(5))