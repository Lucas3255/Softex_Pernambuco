''' 2. Crie uma função chamada dobro que recebe um número como 
parâmetro e retorna o dobro desse número. Teste chamando a função 
com diferentes valores.'''

def dobro(num = 10):
    numDobro = num * 2
    print(f"O dobro de {num} é {numDobro}.")

numero = int(input("Digite um número: "))
dobro(numero)