''' 5. Crie uma função dividir(a, b) que lance (raise) 
uma exceção ZeroDivisionError se b for igual a zero. 
Caso contrário, retorne o resultado da divisão.'''

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("O segundo número precisa ser diferente de zero.")
    else:
        divisao = a / b
        print(f"\n{a} : {b} = {divisao}")
        
num1 = float(input("Digite o 1 número: "))
num2 = float(input("Digite o 2 número: "))

dividir(num1, num2)
