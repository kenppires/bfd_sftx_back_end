#1 - Crie uma classe abstrata "Pessoa" que tenha os métodos: Falar, Andar e Comer e 
# as subclasses Funcionário e Aluno, que herde as características e Métodos de Pessoa. 
# Instancie um objeto para cada subclasse.

from abc import ABC

class Pessoa(ABC):
    def falar(self):
        ...
        
    def andar(self):
        ...

    def comer(self):
        ...

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__

    def falar(self):
        print(f"O funcionário está falando")
        
    def andar(self):
        print(f"O funcionário está andando")
        
    def comer(self):
        print(f"O funcionário está comendo")

class Aluno(Pessoa):
    def __init__(self):
        super().__init__

    def falar(self):
        print(f"O Aluno está falando")
        
    def andar(self):
        print(f"O Aluno está andando")
        
    def comer(self):
        print(f"O Aluno está comendo")

funcionario1 = Funcionario()
aluno1 = Aluno()

print("-Funcionário-")
funcionario1.falar()
funcionario1.andar()
funcionario1.comer()

print("\n-Aluno-")
aluno1.falar()
aluno1.andar()
aluno1.comer()

-