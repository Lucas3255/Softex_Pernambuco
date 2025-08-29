''' 6. Contando frequência de palavras
        Escreva uma função que receba uma lista de palavras e retorne um dicionário 
        com a contagem de cada palavra.
            palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]'''

def contarPalavras(listaPalavras):
    contagem = {}

    for i in listaPalavras:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1

    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
resultado = contarPalavras(palavras)
print(resultado)