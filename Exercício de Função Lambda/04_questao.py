'''
 4. Dada a lista ["uva", "banana", "maçã", "laranja"], ordene 
 as palavras pelo tamanho usando sorted e lambda.
'''

lista = ["uva", "banana", "maçã", "laranja"]

listaOrdenada = sorted(lista, key=lambda palavra: len(palavra))

print("Lista inicial:", lista)
print("Ordenada por tamanho:", listaOrdenada)