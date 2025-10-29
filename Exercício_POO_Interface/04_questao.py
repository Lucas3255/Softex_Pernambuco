'''
 4. Crie uma interface Repositorio com os métodos salvar(objeto) 
 e buscar(id). Depois, crie uma classe RepositorioMemoria que não 
 implemente um dos métodos. O que acontece quando você tenta 
 instanciá-la? Corrija o código.
'''

from abc import ABC, abstractmethod

class Repositorio (ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

#se eu não implementar os métodos anteriores vai dar erro, já que são
#abstratos, é obrigatório usa-los.
class RepositorioMemoria (Repositorio):
    def __init__(self):
        self.dados = {}

    def salvar(self, objeto):
        id = len(self.dados) + 1
        self.dados[id] = objeto
        return f"{objeto.capitalize()} salvo com id {id}."
    
    def buscar(self, id):
        if id in self.dados:
            return f"{self.dados[id]}"
        else:
            return f"Objeto com id {id} não encontrado."

reposit = RepositorioMemoria()

print(reposit.salvar("Relatório de Vendas"))
print(reposit.salvar("Dados Financeiros"))

print("")
print(reposit.buscar(1))
print(reposit.buscar(2))
print(reposit.buscar(50))
