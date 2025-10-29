'''
 3. Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e 
 retorne apenas os 10 maiores notas. No fim imprima na tela a lista desses alunos 
 e suas médias.
'''
import sqlite3 as sql
from pathlib import Path

BaseDir = Path(__file__).resolve().parent
ArquivoBD = BaseDir / "escola_v2.db"

dbConnection = sql.connect(ArquivoBD)

c = dbConnection.cursor()

c.execute("""
          SELECT nome, (nota1 + nota2) / 2.0 as media
          FROM Aluno
          ORDER BY media DESC
          LIMIT 10
          """)

alunos = c.fetchall()

for i, (nome, media) in enumerate(alunos, 1):
    print(f"{i} - {nome} | {media:.1f}")

dbConnection.close()