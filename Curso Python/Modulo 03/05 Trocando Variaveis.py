# Trocando Variaveis em Python 

x = input("Ensira o valor de X: ")
y = input("Ensira o valor de Y: ")

#Criaremos uma variavel temporaria

temp = x 
x = y
y = temp

print(f'O valor de x depois da troca: {x}')
print(f'O valor de y depois da troca: {y}')