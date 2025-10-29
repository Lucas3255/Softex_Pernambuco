''' 4. Crie uma função chamada mensagem que receba um nome como parâmetro 
e exiba a mensagem:
    "Olá, [nome]!"
Caso o nome não seja informado, mostre "Olá, visitante!".'''

def mensagem(nome=None):
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá, visitante!")

nomeUsuario = input("Qual o seu nome: ")
mensagem(nomeUsuario)
