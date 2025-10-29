'''
 4. Na classe Cliente, adicione o atributo saldo. Adicione um método 
 construtor em Cliente que inicialize também os atributos de Usuário 
 usando super().
'''

class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_informacoes(self):
        return f"\n === Acessando Informações ===\n Nome: {self.nome}\n Email: {self.email}\n"

    def saudacao(self):
        return "Olá, usuário."

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)   #super() chama o init da class Usuário
        self.saldo = saldo

    def saudacao(self):
        return "Olá, cliente."


cliente = Cliente("Pedro Gonzales", "pedrogonzales@gmail.com", 1000.00)
usuario = Usuario("João Félix", "joaozinhogameplays@gmail.com")

print(cliente.exibir_informacoes())
print(usuario.exibir_informacoes())

print(cliente.saudacao())
print(usuario.saudacao())

print(f"\nSaldo do cliente: {cliente.saldo:.2f}")