-- SUM Calcule o valor total das mensalidades de todos os cursos. (Use a função SUM)

.tables
.schema Curso

SELECT SUM(mensalidade)
FROM Curso;