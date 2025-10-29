'''
 1. Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma 
 nova lista com o dobro de cada número.
'''

lista = [1, 2, 3, 4, 5]

lista_dobro = list(map(lambda x: x * 2, lista))

print("Lista inicial:", lista)
print("Lista dobrada:", lista_dobro)