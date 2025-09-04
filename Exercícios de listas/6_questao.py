# 6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5].
# Mostre quantas vezes o número 2 aparece na lista.

numeros = [1, 2, 3, 2, 4, 2, 5]
contNum = 0

for i in numeros:
    if i == 2:
        contNum += 1

print(f"Nessa lista tinha {contNum} números 2.")
