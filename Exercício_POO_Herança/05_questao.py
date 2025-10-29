'''
 5. Crie uma classe Funcionario que herda de Usuario e, em seguida, 
 crie uma classe Gerente que herda de Funcionario. Mostre como instanciar 
 um gerente e acessar seus atributos.
'''

class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_informacoes(self):
        return f"\n === Acessando Informações ===\n Nome: {self.nome}\n Email: {self.email}\n"

    def saudacao(self):
        return "Olá, usuário."


class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)   #super() chama o init da class Usuário
        self.saldo = saldo

    def saudacao(self):
        return "Olá, cliente."


class Funcionario(Usuario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario


class Gerente(Funcionario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email, salario)

cliente = Cliente("Pedro Gonzales", "pedrogonzales@gmail.com", 1000.00)
usuario = Usuario("João Félix", "joaozinhogameplays@gmail.com")
funcionario = Funcionario("Carla Carolina", "carlinhadoamor@gmail.com", 10000.00)   #O salário do trabalhador aqui é justo !!!!
gerente = Gerente("Adalberto Costa", "adalbascosta@gmail.com", 15000.00)

print("=== Atributos do Gerente ===")
print(f"Nome: {gerente.nome}")
print(f"Email: {gerente.email}")
print(f"Salário: R$ {gerente.salario:.2f}") 
