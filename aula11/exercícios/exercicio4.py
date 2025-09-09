#4 - Usando a classe Carro, crie um objeto e depois altere o 
# valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.

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
print(20*"-")

carro3 = Carro("Ford","Mustang",1999)
print(carro3)