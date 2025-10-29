'''
 1. Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.
'''

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.livros = []
    
    def ler_livros(self, livro):
        self.livros.append(livro)
        print(f"{self.nome} está lendo {livro.titulo}")

class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
joao = Pessoa("João", 25)
livro = Livro("O Manifesto Comunista", "Karl Marx")

joao.ler_livros(livro)
