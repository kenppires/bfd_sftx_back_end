#3 - Obtenha a media entre nota1 e nota2 dos alunos, 
# ordene em ordem decrescente e retorne apenas os 10 maiores notas. 
# No fim imprima na tela a lista desses alunos e suas médias.

import sqlite3
from pathlib import Path

CAMINHO_DO_DB = 'banco_dados/escola_v2.db' 

conn = None
try:
    conn = sqlite3.connect(CAMINHO_DO_DB)
    cursor = conn.cursor()
    
    top_10 = """
    -- 1. Calcula a média como (nota1 + nota2) / 2
    SELECT 
        nome, 
        (nota1 + nota2) / 2 AS media_final
    FROM 
        Aluno

    -- 2. Ordena o resultado pela média em ordem decrescente (DESC)
    ORDER BY 
        media_final DESC
        
    -- 3. Retorna apenas os 10 maiores
    LIMIT 10;
    """
    cursor.execute(top_10)
    top_10_alunos = cursor.fetchall()
    
    print("\n------- TOP 10 Alunos por Média -------")
    print(40*"-")
    if top_10_alunos:
        for i, (nome, media) in enumerate(top_10_alunos, 1):
            print(f"{i:02d} {nome:<15} {media:.2f}")
    else:
        print("Nenhum registro encontrado na tabela 'Aluno' ou sem notas válidas.")
    print(40*"-")

except sqlite3.Error as e:
    print(f"Ocorreu um erro ao conectar ou executar a query: {e}")

finally:
    if conn:
        conn.close()