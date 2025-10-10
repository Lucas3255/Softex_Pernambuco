'''
 3. Crie uma interface Imprimivel com o método imprimir(). 
 Crie outra interface Exportavel com o método exportar(). 
 Implemente uma classe Relatorio que herde de ambas e 
 implemente os métodos.
'''

from abc import ABC, abstractmethod

class Imprimivel (ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel (ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio (Imprimivel, Exportavel):
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def imprimir(self):
        return f"Relatório de {self.titulo}.\nConteúdo: {self.conteudo}."
    
    def exportar(self):
        return f"Exportando relatório de {self.titulo}."
    
relatorio1 = Relatorio("Vendas Trimestral", "Lucro: 75.000,00")

print(relatorio1.imprimir())
print(relatorio1.exportar())
