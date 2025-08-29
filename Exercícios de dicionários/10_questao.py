''' 10. Ordenando dicionário por valor
        Dado o dicionário:
            pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
        Imprima os itens do dicionário ordenados pela pontuação (valor), 
        o maior para o menor.'''

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

ordenarValores = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)

print("Ranking por pontuação (maior para menor):")
for nome, pontuacao in ordenarValores:
    print(f"{nome}: {pontuacao}")

dicionario_ordenado = dict(ordenarValores)
print(f"\nDicionário ordenado: {dicionario_ordenado}")