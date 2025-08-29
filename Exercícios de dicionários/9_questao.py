''' 9. Mesclando dois dicionários
        Escreva uma função que recebe dois dicionários e retorna
        um novo dicionário contendo todos os pares chave-valor. 
        Se houver chaves repetidas, o valor do segundo dicionário 
        deve prevalecer.'''

def mesclando(d1, d2):
    return d1 | d2

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 4, "d": 5, "e": 6}
resultado = mesclando(d1, d2)
print(resultado)