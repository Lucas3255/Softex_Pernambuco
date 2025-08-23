# 3- Adicione mais dois livros à lista livros usando
# o método append() e exiba a lista atualizada.

livros = ["Olhos Prateados", "Os Distorcidos", "A Última Porta"]

#Add masi 2 livros a lista.
livros.append("Mergulho na Escuridão")
livros.append("Caçador")

for i in livros:
    print(f"{i}", end=", ")