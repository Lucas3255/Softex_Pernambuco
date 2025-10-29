''' 3. Crie uma função chamada soma que receba dois números e 
retorne a soma deles. Depois, use a função para somar 10 + 20.'''

def soma(num1, num2):
    somaNum = num1 + num2
    print(f"Soma: {num1} + {num2} = {somaNum}.")

numero1 = int(input("Digite o 1 número: "))
numero2 = int(input("Digite o 2 número: "))
soma(numero1, numero2)