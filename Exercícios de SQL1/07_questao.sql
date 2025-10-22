-- 7. Liste o ano das turmas e a quantidade de turmas por ano. (Use GROUP BY)

.tables
.schema Turma

SELECT ano, COUNT(*) as quantidade
FROM Turma
GROUP BY ano;