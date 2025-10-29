''' 2. Peça ao usuário dois números e tente multiplicá-los. 
Se o usuário digitar algo inválido, exiba uma mensagem de erro.'''

num = []
result = 0

while True:
    try:
        num1 = float(input("\nDigite o 1 número: "))
        num2 = float(input("Digite o 2 número: "))

        result = num1 * num2

        print(f"\nResultado: {num1} x {num2} = {result}")
        break

    except ValueError:
        input("\nPfvr, digite apenas números.")