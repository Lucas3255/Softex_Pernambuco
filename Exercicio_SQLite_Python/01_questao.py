'''
1. Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
'''

import sqlite3 as sql
from pathlib import Path

ArquivoA = Path(__file__).resolve().parent
ArquivoBD = ArquivoA / "escola_v2.db"

dbConetion = sql.connect(ArquivoBD)
