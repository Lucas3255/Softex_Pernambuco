'''
 6. Crie a classe Casa que é composta por vários Comodos (sala, cozinha, 
 quarto, etc.). Cada Comodo deve ser criado dentro da Casa.
'''

class Comodo():
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        print(f"Cômodo {self.nome} criado com {self.tamanho} m².")
    
class Casa():
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []

        self.comodos.append(Comodo("Sala", 20))
        self.comodos.append(Comodo("Cozinha", 15))
        self.comodos.append(Comodo("Quarta", 12))
        self.comodos.append(Comodo("Banheiro", 8))

        print(f"\nCasa com {len(self.comodos)} cômodos criado em {self.endereco}.")
    
    def listaComodos(self):
        print("\nComodos da casa:")
        for i in self.comodos:
            print(f"- {i.nome}: {i.tamanho} m²")

casa = Casa("Rua Leonardo da Vince, 198")
casa.listaComodos()
