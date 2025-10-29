''' 7. Peça ao usuário dois números e divida o primeiro pelo 
segundo. Trate dois tipos de erro:
    - ValueError se o usuário digitar algo inválido.
    - ZeroDivisionError se tentar dividir por zero.'''

result = 0

while True:
    try:
        num1 = float(input("\nDigite o 1 número: "))
        num2 = float(input("Digite o 2 número: "))

        result = num1 / num2
        print(f"{num1} : {num2} = {result}")
        break
    
    except ValueError:
        print("Pfvr, digite apenas números.")

    except ZeroDivisionError:
        print("Divisão por zero é inválida!")