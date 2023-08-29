"""
Como descobrir se nosso numero eh par
"""

numero = int(input("Insira um numero para saber se relamente eh par: "))
if (numero % 2) == 0: 
    print(f'{numero} eh um numero par')
else: 
    print(f'{numero} eh um numero impar')