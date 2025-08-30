#8 - Dicionário com listas
#Crie um dicionário onde cada chave é o nome de um aluno e 
#o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

notas_alunos = {
    "João": [8, 9, 7],
    "Maria": [9, 10, 8],
    "Pedro": [7, 8, 7]
}

for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    print(f"A média do(a) {aluno} é: {media:.2f}")
