import time

def carregar():
    for i in range(4):
        print(" o")
        time.sleep(0.5)

while True:
    tamanho = int(input("Qual o tamanho sua árvore vai ter?\n >> "))
    tronco = int(tamanho / 2) 

    for i in range(tamanho):
        for a in range(tamanho - i):
            print(" ", end="") 
        for j in range(i * 2 + 1):
            print("o", end="")  
        print()  

    for a in range(tronco):
        for espaco in range(tamanho):
            print(" ", end="") 
        print("|")  

    time.sleep(1)

    escolha = input("-------------------------------\nGostaria de fazer de novo? (s/n)\n >> ").lower()
    if escolha != "s":
        carregar()
        break