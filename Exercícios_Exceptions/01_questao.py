''' 1. Escreva um programa que peça ao usuário para digitar um número. 
Trate o erro caso ele digite algo que não seja um número inteiro.'''

while True:
    try:
        num = int(input("\nDigite um número: "))
        print(f"Você digitou {num}.")
        break
    except ValueError:
        input("\nDigite apenas números.")