''' 3. Crie um programa que peça ao usuário um número inteiro. Se a conversão 
for bem-sucedida, mostre uma mensagem usando o bloco else.'''

try:
    num = input("\nDigite um número inteiro: ")

    inteiro = int(num)

except ValueError:
    input("Pfvr, digite um número válido.")

else:
    print("\nConversão concluída!")
    print(f"Você digitou: {inteiro}.")
    print(f"Tipo do dado: {type(inteiro)}.\n")