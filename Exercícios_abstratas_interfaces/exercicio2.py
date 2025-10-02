#2 - Usando o mesmo exemplo da questão anterior, converta a classe Pessoa em uma interface.

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        ...

    @abstractmethod
    def andar(self):
        ...

    @abstractmethod
    def comer(self):
        ...

class Funcionario(Pessoa):
    def falar(self):
        print(f"O funcionário está falando")

    def andar(self):
        print(f"O funcionário está andando")

    def comer(self):
        print(f"O funcionário está comendo")

class Aluno(Pessoa):
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