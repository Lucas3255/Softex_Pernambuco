'''
 1. Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). 
 Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. 
 Mostre o uso criando objetos e chamando o método falar().
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        return "Auau!"

class Gato(Animal):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Miau!"

tobby = Cachorro("Tobby", 5)
lua = Gato("Lua", 3)

print("Cachorro:", tobby.falar())
print("Gato:", lua.falar())