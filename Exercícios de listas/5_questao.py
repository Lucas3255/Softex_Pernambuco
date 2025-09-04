# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove().
# Se ele não existir, exiba a mensagem "Livro não encontrado".
import time

#Não era pra ser tão grande... mas estava brincando com o código, e deixei assim pq ficou legal.
livros = [
    "Olhos Prateados", "Os Distorcidos", 
    "A Última Porta", "Mergulho na Escuridão", "Caçador"
    ]

while True:
    escolha = int(input('''Gostaria de add Silêncio dos inocentes à lista?\n1 - Sim.\n2 - Não.\n\n>> '''))

    if escolha == 1:
        livros.append("Silêncio dos inocentes")
        break
    elif escolha == 2:
        break
    else:
        print("Dê uma resposta existente pfvr.\n")

if "Silêncio dos inocentes" in livros:
    print("Agora vou remover o livro kkkkkkk")
    time.sleep(1)                               #serve para dar uma pausa temporária.
    livros.remove("Silêncio dos inocentes")
    print("Este livro foi removido XD kkkkkk.")
else:
    print("Livro não encontrado")
