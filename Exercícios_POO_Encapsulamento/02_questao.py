'''
 2. Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, 
 cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os 
 métodos setters e getters para acessar e editar os valores.
'''

class Pessoa():
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade
    
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
    
    def get_identidade(self):
        return self.__identidade
    
    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade

if __name__ == "__main__":
    pessoa = Pessoa("Maria Santas", "25/12/1985", "490.334.234-40", "3490020")

    print("\n=== Informações Iniciais ===")
    print(f"Nome: {pessoa.nome}")
    print(f"Data de Nascimento: {pessoa.data_nascimento}")
    print(f"CPF: {pessoa.get_cpf()}")
    print(f"Identidade: {pessoa.get_identidade()}")

    print("\n" + "="*40 + "\n")

    pessoa.set_cpf("987.654.321-00")
    pessoa.set_identidade("9055523")

    print("=== Informações Atualizadas ===")
    print(f"Nome: {pessoa.nome}")
    print(f"Data de Nascimento: {pessoa.data_nascimento}")
    print(f"CPF: {pessoa.get_cpf()}")
    print(f"Identidade: {pessoa.get_identidade()}\n")