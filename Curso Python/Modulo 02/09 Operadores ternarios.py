"""
Operadores Ternarios
"""
a = 5
b = 8
c = 2

"""if b > a: print("B eh maior do que A")"""

# Operador ternario eh o alinhamento do codigo;
print("B") if b > a else print("A")

if a > b:
    print("A eh maior do que B")
    if a > c:
        print("A eh maior do C")
