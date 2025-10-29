''' 1. Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, 
crie dois objetos dessa classe e imprima os valores de seus atributos.'''

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Arnold Schwarzenegger", 56)
pessoa2 = Pessoa("Mohamed", 23)

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}.")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}.")