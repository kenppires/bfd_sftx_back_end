nota_aluno = float(input("Digite a sua nota: \n"))

if nota_aluno >= 7:
    print("Aluno Aprovado!")

elif nota_aluno < 5:
    print("Aluno Reprovado!")
else:
    print("Aluno em Recuperação!")