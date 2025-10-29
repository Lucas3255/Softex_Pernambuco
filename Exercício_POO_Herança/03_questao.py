'''
 3. Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". 
 Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". 
 Mostre como funciona a chamada.
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
    def __init__(self, nome, email):
        super().__init__(nome, email)   #super() chama o init da class Usuário

    def saudacao(self):
        return "Olá, cliente."


cliente = Cliente("Pedro Gonzales", "pedrogonzales@gmail.com")
usuario = Usuario("João Félix", "joaozinhogameplays@gmail.com")

print(cliente.exibir_informacoes())
print(usuario.exibir_informacoes())

print(cliente.saudacao())
print(usuario.saudacao())
