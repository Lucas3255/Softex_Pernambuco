'''
 6. Usando reduce, calcule o produto (multiplicação) de todos os 
 elementos da lista [2, 3, 4, 5].
'''
from functools import reduce

lista = [2, 3, 4, 5]

multip = reduce(lambda x, y: x * y, lista)

print("Lista:", lista)
print("multiplicação:", multip)