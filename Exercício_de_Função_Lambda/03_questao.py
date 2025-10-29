'''
 3. Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].
'''

from functools import reduce

lista = [1, 2, 3, 4, 5]

soma = reduce(lambda x, y: x + y, lista)

print("Lista:", lista)
print("Soma total:", soma)