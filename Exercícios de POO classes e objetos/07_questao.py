''' 7. Crie uma classe Aluno com atributos nome e nota. 
Depois crie uma classe Turma que tenha uma lista de alunos 
e um método adicionar_aluno(aluno). Crie alguns objetos 
Aluno e adicione-os à turma.'''

# Nesta atividade, eu implimentei uma função __str__ e listar alunos
# para deixar melhor de ter sempre noção dos itens da Turma, não sabia
# que iria ter outra questão apenas sobre isso.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __str__(self):
        return f"{self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} adicionado à turma {self.nome_turma}!")


    def listar_alunos(self):
        print(f"\n=== Turma {self.nome_turma} ===\n")
        for i, aluno in enumerate(self.alunos):
            print(f"{i+1}. {aluno}")

turma1 = Turma("1A")

alunos = [
    Aluno("Lucas Henrique", 8),
    Aluno("Maria Clara", 9.5),
    Aluno("Sérgio Lopes", 5.5)
]

for i in alunos:
    turma1.adicionar_aluno(i)

try:
    nome = input("\nNome do Aluno: ")
    nota = float(input("Informe a nota: "))

    if nota < 0:
        print("\nInforme uma nota igual ou maior que 0.")
    else:
        novo_aluno = Aluno(nome, nota)
        turma1.adicionar_aluno(novo_aluno)
        print("\nAluno Adicionado com Sucesso!")
        turma1.listar_alunos()

except ValueError:
    print("\nInforme uma opção válida.")