'''
 1. Crie uma classe Usuario com atributos nome e email. Depois, 
 crie uma classe Cliente que herde de Usuario. Crie uma instancia 
 de um cliente e acesse todos os atributos.
'''
class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)   #super() chama o init da class Usuário

cliente1 = Cliente("Pedro Gonzales", "pedrogonzales@gmail.com")

print("\n === Acessando Informações ===")
print(f"Nome: {cliente1.nome}")
print(f"Email: {cliente1.email}\n")