tamanho = int(input("Qual o tamanho da arvore: "))
tronco = int(max(1, tamanho / 3))
galhos = 1


for i in range(tamanho):    #define a altura da arvore.
    for j in range(tamanho - i - 1):    #dá espaçamentos.
        print(" ", end="")
 
    for k in range(galhos):
        print("o", end="")


    galhos = galhos + 1 * 2
    print("")


espacos_tronco = tamanho - 1  


for j in range(espacos_tronco):
    print(" ", end="")


for i in range(tronco):
    print("|", end="")
