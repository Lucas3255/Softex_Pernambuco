''' 2. Expanda a classe Pessoa para incluir um método apresentar() 
que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". 
Teste o método chamando-o a partir de um objeto.'''

class Pessoa():                         #Molde 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):       #self puxa os valores contidos no molde (class) para poder ser usado na função.
        print(f"\nOlá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Arnold Schwarzenegger", 56)
pessoa2 = Pessoa("Mohamed", 23)

pessoa1.apresentar()
pessoa2.apresentar()