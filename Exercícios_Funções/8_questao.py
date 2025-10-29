''' 8. Crie uma função chamada calculadora que tenha dentro dela 
outras funções (somar, subtrair, multiplicar, dividir). A função 
principal deve permitir escolher a operação e retornar o resultado.'''

def calculadora():
    def soma(x, y):
        return x + y
    
    def subtracao(x, y):
        return x - y
    
    def multiplicacao(x, y):
        return x * y
    
    def divisao(x, y):
        if y == 0:
            return "Erro: Divisão por zero!"
        return x / y
    
    print("=== Calculadora ===")
    print("Operações disponíveis: +, -, x, :")
    
    try:
        num1 = float(input("\nQual o 1º valor: "))
        num2 = float(input("Qual o 2º valor: "))
        operador = input("Qual operador: ")
        
        match operador:
            case "+":
                resultado = soma(num1, num2)
                print(f"Soma: {resultado}")
            
            case "-":
                resultado = subtracao(num1, num2)
                print(f"Subtração: {resultado}")
            
            case "*" | "x":  # | é o "ou" correto no match case
                resultado = multiplicacao(num1, num2)
                print(f"Multiplicação: {resultado}")
            
            case "/" | ":":
                resultado = divisao(num1, num2)
                print(f"Divisão: {resultado}")
            
            case _:
                print(f"\nOpção '{operador}' inválida.")
                return None
        
        return resultado
        
    except ValueError:
        print("\nErro: Digite números válidos!")
        return None
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        return None

resultado = calculadora()
if resultado is not None:
    print(f"Resultado final: {resultado}")