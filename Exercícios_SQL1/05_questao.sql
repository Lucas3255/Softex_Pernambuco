-- 5. Exiba o nome e a mensalidade de todos os cursos que custam mais de 
-- 600 reais. (Use WHERE com condição numérica).

.tables
.schema Aluno
.schema Curso

SELECT nome, mensalidade
FROM Curso
WHERE mensalidade > 600;