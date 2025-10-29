'''
 3. Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). 
 Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos. 
 Teste criando um objeto e calculando sua área e perímetro.
'''

from abc import ABC, abstractmethod

class FormaGeometrica (ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo (FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return f"Area: {self.base * self.altura:.1f}"

    def perimetro(self):
        return f"Perimetro: {(self.base*2) + (self.altura*2):.1f}"

retangulo1 = Retangulo(4.5,9)
retangulo2 = Retangulo(3, 7)

print(retangulo1.area())
print(retangulo1.perimetro())
print(retangulo2.area())
print(retangulo2.perimetro())
