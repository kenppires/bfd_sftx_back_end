#3 - Crie uma classe Carro com os atributos marca, modelo e ano. 
# Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"
    
carro1 = Carro("Honda","Civic",2011)
carro2 = Carro("VW","Fusca",1995)
carro3 = Carro("Ford","Mustang",2001)

print(carro1)
print(20*"-")
print(carro2)
print(20*"-")
print(carro3)