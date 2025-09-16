#Herança

class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def som(self):
        print("som indefinido")

class Cachorro(Animal):
    def som(self):
        print("'au au'")

dog = Cachorro("Rex", 2)
print(dog.nome)
print(dog.idade)
dog.som()


class Mamifero:
    def __init__(self, idade, habitat, som):
        self.idade = idade
        self.habitat = habitat
        self.som = som
        self.prole = "gestação"
        self.alimentacao_infantil = "leite"
    
    def som(self):
        return "Nenhum som definido"

class Morcego(Mamifero):
    def __init__(self, idade, habitat, som):
        super().__init__(idade, habitat, som)
        self.locomocao = "vôo"  

morcego = Morcego(1, "caverna", "chiado")

print(40*"_")
print(morcego.idade)
print(morcego.habitat)
print(morcego.som)
print(morcego.locomocao)