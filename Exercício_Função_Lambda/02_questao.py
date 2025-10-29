'''
 2. Dada a lista [10, 15, 20, 25, 30], use filter com lambda para 
 obter apenas os números pares.
'''

lista = [10, 15, 20, 25, 30]

numPares = list(filter(lambda x: x % 2 == 0, lista))

print("Lista:", lista)
print("Números pares:", numPares)