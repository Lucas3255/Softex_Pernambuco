'''
 2. Faça a query para pegar toda a tabela alunos e imprima na tela.
'''

import sqlite3 as sql
from pathlib import Path

#Passei 30 min mexendo nisso, n ironicamente, oq importa é q deu certo,
#O arquivo do Banco corrompeu por algum motivo.
ArquivoA = Path(__file__).resolve().parent
ArquivoBD = ArquivoA / "escola_v2.db"

dbConnection = sql.connect(ArquivoBD)

c = dbConnection.cursor()

c.execute("""
          SELECT *
          FROM Aluno
          """)

alunos = c.fetchall()  

for aluno in alunos:
    print(aluno)

dbConnection.close()    #Encerra conexão com o BD.