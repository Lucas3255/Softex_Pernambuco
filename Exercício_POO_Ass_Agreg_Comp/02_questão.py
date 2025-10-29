'''
 2. Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.
'''

class Aluno():
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
    
    def pegar_onibus(self, onibus):
        print(f"{self.nome} pegou o ônibus {onibus.nome} para ir a escola.")

class Onibus():
    def __init__(self, nome, linha):
        self.nome = nome
        self.linha = linha

aluno = Aluno("José Maria", 13, 23199)
onibus1 = Onibus("TI TIP", 201)

aluno.pegar_onibus(onibus1)
