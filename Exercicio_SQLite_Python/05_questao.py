'''
 5. Usando a query da questão 4, adicione um filtro para pegar apenas os 
 alunos da turma 2 e imprima na tela.
'''

import sqlite3 as sql
from pathlib import Path

BaseDir = Path(__file__).resolve().parent
ArquivoBD = BaseDir / "escola_v2.db"

dbConnection = sql.connect(ArquivoBD)
c = dbConnection.cursor()

c.execute("""
          SELECT *
          FROM Aluno
          LEFT JOIN Turma ON Aluno.id_turma = Turma.id
          WHERE Aluno.id_turma = 2
          """)

result = c.fetchall()

for i in result:
    print(i)

dbConnection.close()