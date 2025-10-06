'''
 7. Dada a lista ["banana", "uva", "maçã", "laranja"], ordene 
 as palavras pelo último caractere.
'''
#Essa eu fiquei uma pouco em dúvida, n sei se é isso.

lista = ["banana", "uva", "maçã", "laranja"]

novaLista = sorted(lista, key=lambda palavra: palavra[-1])

print("Lista inicial:", lista)
print("Nova lista:", novaLista)