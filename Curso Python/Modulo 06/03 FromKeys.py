#index      0        1        2
tupla = ("item1", "item2", "item3")
tupla2 = ("item1", "item2", "item3")
dicio = dict.fromkeys(tupla, tupla2)
print(dicio)

dicio = {
    "dicio1": {
        "nome": "Ana",
        "idade": 38
    },
    "dicio2": {
            "nome": "Pedro",
            "idade": 38,
            "dicio3": {
                "nome": "Ana Julia",
                "idade": 5
            }
        }
}

print(dicio)
