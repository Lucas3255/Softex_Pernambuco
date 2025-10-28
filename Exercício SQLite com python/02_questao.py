'''
 2. Faça a query para pegar toda a tabela alunos e imprima na tela.
'''

import sqlite3 as sql

dbConnection = sql.connect('BD/escola_v2.db')

c = dbConnection.cursor()

c.execute("SELECT * FROM Aluno")

alunos = c.fetchall()  

for i in alunos:
    print(i)

dbConnection.close()    #Encerra conexão com o BD.