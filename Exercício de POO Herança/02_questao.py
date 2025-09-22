'''
 2. Implemente um método exibir_informacoes() na classe Usuario e 
 herde esse método em Cliente. Mostre como chamar o método herdado 
 a partir de um objeto Cliente.
'''

class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_informacoes(self):
        return f"\n === Acessando Informações ===\n Nome: {self.nome}\n Email: {self.email}\n"


class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)   #super() chama o init da class Usuário


cliente1 = Cliente("Pedro Gonzales", "pedrogonzales@gmail.com")
print(cliente1.exibir_informacoes())
