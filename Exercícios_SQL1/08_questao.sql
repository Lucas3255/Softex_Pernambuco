-- 8. Calcule a média da nota1 dos alunos por turma_id. (Use GROUP BY com função de agregação)

.tables
.schema Aluno

SELECT id_turma, AVG(nota1) as media
FROM Aluno
GROUP BY id_turma;