''' 3. Crie uma classe Carro com os atributos marca, modelo e ano. 
Use o método __init__ para inicializar esses valores. Crie três 
objetos e mostre suas informações.'''

class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Toyota", "Corolla", 2023)
carro2 = Carro("Volkswagen", "Golf", "2022")
carro3 = Carro("Ford", "Mustang", 2024)

print(f"\nMarca: {carro1.marca}, Modelo: {carro1.modelo}, Ano: {carro1.ano}.")
print(f"Marca: {carro2.marca}, Modelo: {carro2.modelo}, Ano: {carro2.ano}.")
print(f"Marca: {carro3.marca}, Modelo: {carro3.modelo}, Ano: {carro3.ano}.\n")