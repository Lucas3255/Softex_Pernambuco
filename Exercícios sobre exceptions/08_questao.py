''' 8. Crie um programa que peça ao usuário um número inteiro 
e verifique se ele é par. Use:
    - try para a conversão.
    - else para verificar se é par ou ímpar.
    - finally para exibir "Fim do programa".'''

try:
    num = int(input("Digite um número: "))

except ValueError:
    print("Digite apenas números inteiros.")

else:
    if num == 0:
        print(f"O número é {num}.")
    elif num % 2 == 0:
        print(f"O número {num} é PAR!")
    else:
        print(f"O número {num} é ÍMPAR!")

finally:
    print("\nFim do Programa.\n")