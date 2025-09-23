'''
 7. Usando o exemplo anterior, adicione um método status() em Autenticacao e 
 também em Permissao. Se a classe Administrador herda das duas, qual versão 
 de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.
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
        
    def status(self):
        return "Status da Autenticacao: Sistema de Login Ativo."


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
        
    def status(self):
        return "Status da Permissao: Sistema de permissões ativo"


class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome

    def fazerLogin(self, usuario, senha):
        return self.login(usuario, senha)
    
    def verificarPermissao(self, usuario, recurso):
        return self.verificar_permissao(usuario, recurso)
    
    def testar_status(self):
        return self.status()
    

adm = Administrador("Pedro Cavalcante")

print("")
print(Administrador.__mro__)

print(adm.fazerLogin("adm", "adm123"))
print(adm.fazerLogin("adm", "dfhgsh"))

print("")
print(adm.verificarPermissao("adm", "excluir"))
print(adm.verificarPermissao("usuario", "excluir"))
print("")

print(adm.status())
print(adm.testar_status())
print("")
