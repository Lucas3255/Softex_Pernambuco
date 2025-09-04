''' 6. Crie uma função chamada media que receba uma quantidade 
variável de números e retorne a média deles. Teste com 3, 5 e 7 
valores diferentes.'''

def media(*x):
    mediaValor = 0
    for i in x:
        mediaValor += i

    mediaFinal = mediaValor / len(x)
    print(x)
    print(mediaFinal)

num = []

valor = int(input("Quantos números quer calcular: "))

for i in range(valor):
    num.append(float(input(f"Digite o {i+1} número: ")))

media(*num)