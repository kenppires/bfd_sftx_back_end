#4 - Use Left Join com as tabelas Aluno e Turma e 
# imprima todos os dados da tabela.

import sqlite3
from pathlib import Path

CAMINHO_DO_DB = 'banco_dados/escola_v2.db' 

conn = None
try:
    conn = sqlite3.connect(CAMINHO_DO_DB)
    cursor = conn.cursor()

    query_left_join = """
    SELECT 
        A.*,
        T.*
    FROM 
        Aluno AS A
    LEFT JOIN 
        Turma AS T ON A.id_turma = T.id;
    """

    cursor.execute(query_left_join)
    dados_join = cursor.fetchall()

    if not dados_join:
        print("Nenhum dado encontrado para o JOIN.")
    else:
        col_names = [description[0] for description in cursor.description]
        
        print("|".join(col_names))

        for row in dados_join:
            row_str = "|".join(str(item) if item is not None else 'NULL' for item in row)
            print(row_str)

except sqlite3.Error as e:
    print(f"Ocorreu um erro ao conectar ou executar a query: {e}")

finally:
    if conn:
        conn.close()