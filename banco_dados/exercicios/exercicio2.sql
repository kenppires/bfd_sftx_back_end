--1 - COUNT Mostre quantos alunos estão cadastrados 
--na tabela Aluno. (Use a função COUNT)
SELECT
    COUNT(*) AS total_alunos
FROM
    Aluno;

--2 - MIN Mostre a menor mensalidade entre todos os 
--cursos cadastrados. (Use a função MIN)
SELECT
    MIN(mensalidade) AS menor_mensalidade
FROM
    curso;

--3 - MAX Mostre a maior nota1 registrada entre todos 
--os alunos. (Use a função MAX)
SELECT
    MAX(nota1) AS maior_nota1
FROM
    Aluno;

--4 - SUM Calcule o valor total das mensalidades de 
--todos os cursos. (Use a função SUM)
SELECT
    SUM(mensalidade) AS total_mensalidades
FROM
    curso;

--5 - AVG Mostre a média geral da nota2 dos alunos. (Use a função AVG)
SELECT
    AVG(nota2) AS media_geral_nota2
FROM
    Aluno;