--1 - Mostre todos os registros da tabela Aluno. 
--(Use SELECT e FROM)
SELECT * 
FROM Aluno;

--2 - Exiba apenas o nome e a nota1 de todos os alunos. 
--(Use SELECT com colunas específicas)
SELECT nome, nota1
FROM Aluno;

--3 - Liste todos os alunos cuja nota2 seja maior que 8.
--(Use WHERE)
SELECT nome, nota2
FROM Aluno
WHERE nota2 > 8;


--4 - Mostre os alunos que nasceram após o ano de 2000.
--(Use WHERE com data)
SELECT nome, data_nascimento
FROM Aluno
WHERE data_nascimento > 2000;

--5 - Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais.
--(Use WHERE com condição numérica)
SELECT * 
FROM Curso
WHERE mensalidade > 600;

--6 - Mostre o nome das turmas e o ano correspondente, 
--ordenados pelo ano em ordem crescente.(Use ORDER BY)
SELECT
    nome,
    ano
FROM
    turma
ORDER BY
    ano ASC;

--7 - Liste o ano das turmas e a quantidade de turmas por ano.
--(Use GROUP BY)
SELECT
    ano,
    COUNT(*) AS quantidade_turmas
FROM
    turma
GROUP BY
    ano;

--8 - Calcule a média da nota1 dos alunos por turma_id.
--(Use GROUP BY com função de agregação)
SELECT
    id_turma,
    ROUND(SUM(nota1) / COUNT(nota1), 1) AS media_nota1
FROM
    aluno
GROUP BY
    id_turma;

--9 - Mostre o ano e a quantidade de turmas apenas para 
--os anos que têm mais de 2 turmas.(Use GROUP BY e HAVING)
SELECT
    ano,
    COUNT(*) AS quantidade_turmas
FROM
    turma
GROUP BY
    ano
HAVING
    COUNT(*) > 2;

--10 - Exiba o nome dos cursos e suas mensalidades, 
--ordenando primeiro pela mensalidade (decrescente).(Use ORDER BY)
SELECT nome, mensalidade
FROM Curso
ORDER BY mensalidade DESC; 
