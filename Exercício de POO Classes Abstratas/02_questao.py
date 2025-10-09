'''
 2. Tente instanciar diretamente a classe Animal da questão anterior 
 e explique o erro gerado pelo Python.
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

#Não tenho certeza, mas acho q já está instanciado.
tobby = Cachorro("Tobby", 5)
lua = Gato("Lua", 3)

print("Cachorro:", tobby.falar())
print("Gato:", lua.falar())