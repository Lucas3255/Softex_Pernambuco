#10- Use input para receber 3 notas de dois alunos. As notas de cada
# aluno precisam ser armazenadas em uma lista separada que deve ser
# armazenada dentro de outra lista chamada notas, exemplo: 
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

alunoA = []
alunoB = []
somaA = 0
somaB = 0

print("Notas do 1 Aluno:")
for i in range(3):
    nota = float(input(f"{i+1} nota: "))
    alunoA.append(nota)
    somaA += nota

print("\nNotas do 2 Aluno:")
for i in range(3):
    nota = float(input(f"{i+1} nota: "))
    alunoB.append(nota)
    somaB += nota

mediaA = somaA / 3
mediaB = somaB / 3
notas = [alunoA, alunoB]

print(f"\nLista de notas: {notas}.")
print(f"A média do Aluno A foi {mediaA:.1f}.")
print(f"A média do Aluno B foi {mediaB:.1f}.")
