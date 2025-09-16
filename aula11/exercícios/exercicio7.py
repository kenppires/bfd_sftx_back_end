#7 - Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha 
# uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado à turma.")

aluno1 = Aluno("João", 8.5)
aluno2 = Aluno("Maria", 9.0)
aluno3 = Aluno("Pedro", 7.5)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)