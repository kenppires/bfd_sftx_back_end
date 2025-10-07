#1 - Crie uma classe abstrata "Pessoa" que tenha os métodos: Falar, Andar e Comer e 
# as subclasses Funcionário e Aluno, que herde as características e Métodos de Pessoa. 
# Instancie um objeto para cada subclasse.

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        print(f"O {self.__class__.__name__} está falando...")

    @abstractmethod
    def andar(self):
        print(f"O {self.__class__.__name__} está andando...")

    @abstractmethod
    def comer(self):
        print(f"O {self.__class__.__name__} está comendo...")

class Funcionario(Pessoa):
    def falar(self):
        return super().falar()

    def andar(self):
        return super().andar()
        
    def comer(self):
        return super().comer()

class Aluno(Pessoa):
    def falar(self):
        return super().falar()

    def andar(self):
        return super().andar()
        
    def comer(self):
        return super().comer()

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
