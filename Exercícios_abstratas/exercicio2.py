#1 - Proibição de instanciamento
#Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print(f"AU AU")

class Gato(Animal):
    def falar(self):
        print(f"Meow")

dog1 = Cachorro()

cat1 = Gato()

dog1.falar()

cat1.falar()


# Exibe erro porque a classe abstrata Animal serve apenas como modelo e não pode ser instanciada diretamente.
animal1 = Animal()
