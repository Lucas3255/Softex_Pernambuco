''' 4. Usando a classe Carro, crie um objeto e depois altere o 
valor de um de seus atributos (por exemplo, mudar o ano). Imprima 
antes e depois da alteração.'''

class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Toyota", "Corolla", 2023)

print("\n=== Antes da Alteração ===")
print(f"Marca: {carro1.marca}.\nModelo: {carro1.modelo}.\nAno: {carro1.ano}.")

carro1.ano = 2024

print("\n=== Depois da Alteração ===")
print(f"Marca: {carro1.marca}.\nModelo: {carro1.modelo}.\n Ano: {carro1.ano}.\n")