#9 - Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos 
# de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.

class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

meu_cachorro = Cachorro("Rex", 5)

print(f"[V1 Objeto]: {meu_cachorro.nome} é da espécie {meu_cachorro.especie}")

print(f"[V2 Classe]: A espécie de cachorro é {Cachorro.especie}")