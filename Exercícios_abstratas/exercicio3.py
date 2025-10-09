#3 - Múltiplos métodos abstratos
#Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: 
# area() e perimetro(). Crie uma classe concreta Retangulo que herde de FormaGeometrica e 
# implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro.

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

    
retangulo1 = Retangulo(base=10, altura=5)

area = retangulo1.area()
print(f"Área do retângulo: {area}")
perimetro = retangulo1.perimetro()
print(f"Perímetor do retângulo: {perimetro}")