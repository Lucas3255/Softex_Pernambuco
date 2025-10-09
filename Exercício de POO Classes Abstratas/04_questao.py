'''
 4. Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). 
 Depois, crie uma subclasse Carro que implemente apenas o método mover(). O que acontece 
 quando você tenta instanciar Carro? Corrija implementando o segundo método.
'''

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    #O erro veio nesse trecho, já q eu n estava utilizando o método.
    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "Carro se movendo"
    
    #Para corrigir o erro, ou que excluo o método ou eu utilizo.
    #Neste caso, eu utilizei.
    def parar(self):
        return "Freiando para não capotar."
    

carro1 = Carro()

print(carro1.mover())
print(carro1.parar())