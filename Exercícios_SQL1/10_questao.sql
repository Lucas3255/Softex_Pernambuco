-- 10. Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade (decrescente). (Use ORDER BY)

.tables
.schema Curso

SELECT nome, mensalidade
FROM Curso
ORDER BY mensalidade DESC;