''' 8. Dicionário com listas
        Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma 
        lista com 3 notas. Depois, imprima a média de cada aluno.'''

alunos = {
    "Arthur Cervero": [7.5, 8.0, 6.5],
    "Joui Jouki": [9.0, 8.5, 9.5],
    "Kaiser Cohen": [6.0, 7.0, 5.5],
}

print("\nMédias dos alunos:\n")

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno}: {media:.2f}")
