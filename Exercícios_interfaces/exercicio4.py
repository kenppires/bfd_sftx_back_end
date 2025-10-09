#4 - Forçando contrato
#Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). 
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. 
# O que acontece quando você tenta instanciá-la? Corrija o código.

from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    @abstractmethod
    def buscar(id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return f"O Objeto: '{objeto}' foi encontrado no repositório."

#2.implementado após o erro
    def buscar(self, id):
        return f"O ID: '{id}' foi encontrado no repositório."


objeto1 = RepositorioMemoria()

print(objeto1.salvar("PC"))

print(objeto1.buscar(152))

#1.Ele não permite instanciar a classe RepositorioMemoria sem implementar o método "buscar" e exibe o erro::
#TypeError: Can't instantiate abstract class RepositorioMemoria without an implementation for abstract method 'buscar'