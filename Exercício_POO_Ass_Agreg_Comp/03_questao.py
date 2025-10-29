'''
 3. Crie uma classe Funcionario e Departamento que contém uma lista 
 de Funcionarios.Departamento deve agregar funcionários já criados.
'''

class Funcionario():
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"{self.nome}: {self.cargo}"
    
class Departamento():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionarFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.nome} é do {self.nome}.")
    
    def listarFuncionarios(self):
        print(f"\nFuncionários do {self.nome}: ")
        for i in self.funcionarios:
            print(f"- {i}")

func1 = Funcionario("Joey", "Gerente")
func2 = Funcionario("Ellie", "Atendente")

depart = Departamento("Almoxarifado")

depart.adicionarFuncionario(func1)
depart.adicionarFuncionario(func2)

depart.listarFuncionarios()

