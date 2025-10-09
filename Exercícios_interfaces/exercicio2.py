#2 - Interface múltipla
#Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). 
# Crie uma classe Computador que implemente ambas. Mostre seu uso.

from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return f"O {self.__class__.__name__} foi ligado!"

    def desligar(self):
        return f"O {self.__class__.__name__} foi desligado!"

pc1 = Computador()
   
print(pc1.ligar())
print(40*"-")
print(pc1.desligar())