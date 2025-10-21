/*
SQL - Structured Query Language
Usando SQLite

Requisitos:
- Instalar extensão:
    - sqlite do Alexcvzz
    - https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite
*/

-- Comando para listar as tabelas do BD
.tables

-- Mostra o esquema de criação da tabela
.schema Aluno

-- Retorna todas as colunas da tabela Aluno
SELECT *
FROM Aluno;

-- Retorna apenas a coluna nome da tabela Aluno
SELECT nome
FROM Aluno;

-- Retorna as colunas nome, nota1 e nota2 da tabela Aluno
SELECT 
    nome,
    nota1,
    nota2
FROM Aluno;

-- Retorna as colunas nome e nota1 apenas com os registros com nota1 maior ou igual a 7
SELECT nome, nota1
FROM Aluno
WHERE nota1 >= 7;

-- Retorna Retorna as colunas nome, nota1, nota2, apenas com os registros com nota1 e nota2 maior ou igual a 7
SELECT nome, nota1, nota2
FROM Aluno
WHERE nota1 >= 7 AND nota2 >=7;

-- Retorna Retorna as colunas nome, nota1, nota2, e uma coluna com a média das notas.
SELECT 
    nome, 
    nota1,
    nota2,
    (nota1+nota2)/2
FROM Aluno;

-- Mesmo que anterior, mas informando um alias/apelido para a coluna de média.
SELECT 
    nome, 
    nota1,
    nota2,
    (nota1+nota2)/2 AS media
FROM Aluno;

-- Ordena a tabela com em ordem decrescente com base nas médias.
SELECT 
    nome nome_aluno, 
    nota1,
    nota2,
    (nota1+nota2)/2 AS media_notas
FROM Aluno
ORDER BY media_notas DESC;

-- Mesmo que o anterior, mas retornando apenas os registros com as 10 maiores médias.
SELECT 
    nome nome_aluno, 
    nota1,
    nota2,
    (nota1+nota2)/2 AS media_notas
FROM Aluno
ORDER BY media_notas DESC
LIMIT 10;

-- Agrupa os dados com base no id_turma
SELECT id_turma
FROM Aluno
GROUP BY id_turma;

-- Agrupa os dados com base no id_turma e retorna a contagem de alunos por turma
SELECT id_turma, COUNT() AS n_alunos
FROM Aluno
GROUP BY id_turma;

-- Agrupa os dados com base no id_turma e retorna as turmas com mais de 20 alunos
SELECT id_turma, COUNT() AS n_alunos
FROM Aluno
GROUP BY id_turma
HAVING n_alunos > 20;