''' 6. Crie uma exceção personalizada chamada IdadeInvalidaError. 
Depois, crie uma função cadastrar_idade(idade) que lance essa 
exceção caso a idade seja negativa.'''

class IdadeInvalidaError(Exception):
    def __init__(self, idade):
        mensagem = f"É impossivel você ter {idade}, digite uma idade válida."
        
        super().__init__(mensagem)
        self.idade = idade


def cadastrar_idade(idade):
    if idade <= 0:
        raise IdadeInvalidaError(idade)


try:
    num = int(input("Digite sua idade: "))
    cadastrar_idade(num)
    print(f"Idade {num} cadastrada com sucesso!")

except ValueError:
    print("Digite apenas números inteiros!")

except IdadeInvalidaError as e:
    print(e)