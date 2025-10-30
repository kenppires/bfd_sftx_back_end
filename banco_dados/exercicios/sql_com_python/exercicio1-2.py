#1 - Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
#2 - Faça a query para pegar toda a tabela alunos e imprima na tela.

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

DB_PATH = BASE_DIR / "db" / "escola_v2.db"
print(DB_PATH)

db_connection = sqlite3.connect('banco_dados/escola_v2.db')

cursor = db_connection.cursor()

cursor.execute("""
SELECT * 
FROM Aluno
""")

query_result = cursor.fetchall()

print(query_result)

db_connection.close()