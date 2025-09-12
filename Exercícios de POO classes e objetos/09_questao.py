''' 9. Crie uma classe Cachorro com um atributo de classe 
especie = "Canis familiaris" e atributos de instância nome 
e idade. Mostre a diferença entre acessar especie pelo objeto 
e pela classe.'''

class Cachorro:
    especie = "Canis familiaris"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} - {self.idade} anos."
    
spike = Cachorro("Spike", 3)
luna = Cachorro("Luna", 7)
loren = Cachorro("Loren", 2)

print("\n===Acessando Doguinhos por Objeto ===")
print(f"Nome = {spike.nome}, Idade = {spike.idade}")
print(f"Nome = {luna.nome}, Idade = {luna.idade}")
print(f"Nome = {loren.nome}, Idade = {loren.idade}\n")

print(f"=== Acessando pela Classe ===")
print(f"{spike.nome} = {spike.especie}")
print(f"{luna.nome} = {luna.especie}")
print(f"{loren.nome} = {loren.especie}\n")