# 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().

livros = [
    "Olhos Prateados", "Os Distorcidos", 
    "A Última Porta", "Mergulho na Escuridão", "Caçador"]

#como pede q seja n 2 posição, coloco 1, já q seria: livros[0, 1, 2, ...]
livros.insert(1, "Duna")
print(f"{livros[1]}.")
for i in livros:
    print(f"{i}", end=", ")