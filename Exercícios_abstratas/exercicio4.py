#4 - Herança parcial
# Crie uma classe abstrata Transporte com dois métodos abstratos: 
# mover() e parar(). Depois, crie uma subclasse Carro que implemente apenas o método mover(). 
# O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        return f"O carro está se movendo"

#2.implementado após o erro
    def parar(self):
        return f"O Carro está parado"

#1.Ele não permite instanciar a classe Carro sem implementar o método "parar" e exibe o erro:
# "TypeError: Can't instantiate abstract class Carro without an implementation for abstract method 'parar'"

carro1 = Carro()

print(carro1.parar())
print(40*"-")
print(carro1.mover())