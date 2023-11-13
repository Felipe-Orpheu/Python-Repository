"""
tupla = ("item1",)
tupla2 = ("a", "b")

tupla = "item1", "item2", "item3" 
print(tupla)

for x in tupla: 
    print(x)

for x in range(len(tupla)): 
    print(x, tupla[x])
"""

tupla = ("item1", "item2", "item3")
print(tupla)

(x, y, z) = tupla
print("x:",x)
print("y:",y)
print("z:",z)

