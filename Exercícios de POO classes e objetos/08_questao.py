''' 8. Na classe Aluno, implemente o método __str__ para que, 
ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria 
- Nota: 9.5". Teste imprimindo os objetos.'''

# Essa questão é igual a 7, fiz adições na outra sem saber dessa questão!

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