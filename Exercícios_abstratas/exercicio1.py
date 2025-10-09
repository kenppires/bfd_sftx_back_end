#1 - Definição de classe abstrata
# Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). 
# Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. 
# Mostre o uso criando objetos e chamando o método falar().

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