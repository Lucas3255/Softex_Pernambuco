''' 7. Invertendo um dicionário
        Dado o dicionário:
            d = {"a": 1, "b": 2, "c": 3}
        Crie um novo dicionário invertendo as chaves e os 
        valores: {1: "a", 2: "b", 3: "c"}.'''

def inversaoValores(dicio):
    d_inverso = {}

    for tipoDado, valor in dicio.items():
        d_inverso[valor] = tipoDado

    return d_inverso

d = {
    "a": 1, 
    "b": 2, 
    "c": 3
    }
result = inversaoValores(d)
print(result)
