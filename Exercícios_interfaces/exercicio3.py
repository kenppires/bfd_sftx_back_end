#3 - Interface em herança múltipla
#Crie uma interface Imprimivel com o método imprimir(). Crie outra interface Exportavel com o método exportar(). 
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

from abc import ABC, abstractmethod

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return "O Relatório está sendo impresso..."
    
    def exportar(self):
        return "O Relatório será exportado..."

relatorio1 = Relatorio()

print(relatorio1.imprimir())
print(40*"-")
print(relatorio1.exportar())

