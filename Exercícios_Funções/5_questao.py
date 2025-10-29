''' 5. Crie uma função chamada operacoes que receba dois números e 
retorne a soma, a subtração e a multiplicação deles.'''

def operacoes(num1, num2):
    soma = num1 + num2
    subt = num1 - num2
    mult = num1 * num2

    print(f"Soma: {num1} + {num2} = {soma}")
    print(f"Subtração: {num1} - {num2} = {subt}")
    print(f"Multiplicação: {num1} x {num2} = {mult}")

numero1 = int(input("Digite o 1 número: "))
numero2 = int(input("Digite o 2 número: "))
operacoes(numero1, numero2)