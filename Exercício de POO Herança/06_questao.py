'''
 6. Crie uma classe Autenticacao com um método login(). Crie outra 
 classe Permissao com um método verificar_permissao(). Em seguida, 
 crie uma classe Administrador que herda de ambas. Como usar os 
 métodos herdados?
'''

class Autenticacao():
    def login(self, usuario, senha):
        usuarios_validos = {
            "adm": "adm123",
            "gerente": "gerente123",
            "usuario": "usuario123"
        }

        if usuario in usuarios_validos[usuario] == senha:
            return f"\nLogin realizado com Sucesso para {usuario}."
        else:
            return "Falha no Login!"

class Permissao():
    def verificar_permissao(self, usuario, recurso):
        permissoes = {
            "adm": ["cadastrar", "excluir", "editar", "vizualizar"],
            "gerente": ["editar", "vizualizar"],
            "usuario": ["vizualizar"]
        }

        if usuario in permissoes and recurso in permissoes[usuario]:
            return f"Permissão Condedida: {usuario} pode {recurso}."
        else:
            return f"Permissão Negada! {usuario} não pode {recurso}."

class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome

    def fazerLogin(self, usuario, senha):
        return self.login(usuario, senha)
    
    def verificarPermissao(self, usuario, recurso):
        return self.verificar_permissao(usuario, recurso)
    

adm = Administrador("Pedro Cavalcante")

print("")
print(adm.fazerLogin("adm", "adm123"))
print(adm.fazerLogin("adm", "dfhgsh"))

print("")
print(adm.verificarPermissao("adm", "excluir"))
print(adm.verificarPermissao("usuario", "excluir"))
print("")