-- 9. Mostre o ano e a quantidade de turmas apenas para os anos que 
-- têm mais de 2 turmas. (Use GROUP BY e HAVING)

.tables
.schema Turma

SELECT ano, COUNT(*) as quantidade
FROM Turma
GROUP BY ano
HAVING COUNT(*) > 2;