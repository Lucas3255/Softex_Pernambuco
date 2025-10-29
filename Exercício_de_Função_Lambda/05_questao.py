'''
 5. Dada a lista ["ana", "pedro", "maria"], use map e lambda para 
 transformar em ["Ana", "Pedro", "Maria"].
'''

lista = ["ana", "pedro", "maria"]

novaLista = list(map(lambda nome: nome.capitalize(), lista))

print("Lista inicial:", lista)
print("Nova lista:", novaLista)