#Questão 10: Receber notas de dois alunos e calcular a média

notas = []

for i in range(2):
    notas_aluno = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1} do aluno {i + 1}: "))
        notas_aluno.append(nota)
    notas.append(notas_aluno)

for i in range(len(notas)):
    media = sum(notas[i]) / 3
    print(f"A média do aluno {i + 1} é: {media:.2f}")