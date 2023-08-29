"""
do while 

Codigo para a divinhar um numero 
"""

palpite = 5
numero = 9 

while True: #Nós verificamos sem executar
    print("Qual o numero correto? ")
    palpite = int(input())
    if palpite == numero: #Estamos verificando o codigo
        print("Parabens. Você acertou!!!")
        break
    else: 
        print("Voce Errou")
else: 
    print("Erro na aplicação")
    print(bool(palpite))