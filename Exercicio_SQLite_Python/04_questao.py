'''
 4. Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
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
          """)

result = c.fetchall()

for i in result:
    print(i)

dbConnection.close()