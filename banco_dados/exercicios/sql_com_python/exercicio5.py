#5 - Usando a query da questão 4, adicione um filtro para
# pegar apenas os alunos da turma 2 e imprima na tela.

import sqlite3
from pathlib import Path

CAMINHO_DO_DB = 'banco_dados/escola_v2.db' 

conn = None
try:
    conn = sqlite3.connect(CAMINHO_DO_DB)
    cursor = conn.cursor()

    left_join_filer = """
    SELECT 
        A.*,
        T.*
    FROM 
        Aluno AS A
    LEFT JOIN 
        Turma AS T ON A.id_turma = T.id
    WHERE 
        A.id_turma = 2; -- Filtro para Turma 2
    """

    cursor.execute(left_join_filer)
    join_filter = cursor.fetchall()

    if not join_filter:
        print("Nenhum dado encontrado para a Turma 2.")
    else:
        col_names = [description[0] for description in cursor.description]
        
        print("|".join(col_names))

        for row in join_filter:
            row_str = "|".join(str(item) if item is not None else 'NULL' for item in row)
            print(row_str)

except sqlite3.Error as e:
    print(f"Ocorreu um erro ao conectar ou executar a query: {e}")

finally:
    if conn:
        conn.close()