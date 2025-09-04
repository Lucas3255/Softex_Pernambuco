''' 9. Crie uma função chamada aplicar_operacao que receba dois 
números e uma função como parâmetros. A função deve aplicar a 
operação recebida (ex: soma, multiplicação).
Exemplo:
    def soma(a, b): return a + b
    aplicar_operacao(3, 4, soma)'''

def aplicar_operacao(num1, num2, operacao):
    return operacao(num1, num2)

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

resultado1 = aplicar_operacao(3, 4, soma)
print(f"Soma: 3 + 4 = {resultado1}")

resultado2 = aplicar_operacao(5, 3, multiplicacao)
print(f"Multiplicação: 5 x 3 = {resultado2}")

resultado3 = aplicar_operacao(10, 2, divisao)
print(f"Divisão: 10 ÷ 2 = {resultado3}")