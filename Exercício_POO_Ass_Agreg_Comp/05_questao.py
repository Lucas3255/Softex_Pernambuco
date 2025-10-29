'''
 5. Crie a classe Carro que possui um Motor. O Motor deve ser 
 criado dentro do Carro. Se o Carro deixar de existir, o Motor 
 também deixa. Mostre isso criando e depois apagando o objeto.
'''

class Motor():
    def __init__(self, potencia):
        self.potencia = potencia
        print(f"O moto com {self.potencia} cavalos foi criado!")

    def __del__(self):
        print(f"Moto deixou de existir... Baforizou e Evaporou.")
    
class Carro():
    def __init__(self, modelo, potenciaMotor):
        self.modelo = modelo
        self.motor = Motor(potenciaMotor)
        print(f"Carro {self.modelo} criado!")
    
    def __del__(self):
        print(f"Carro {self.modelo} faleceu, virou sucata.")

print("\n=== Criando carro ===")
carro1 = Carro("Fusca", 40)

print("\n=== Destruindo o Infeliz ===")
del carro1
print("")
