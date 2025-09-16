#1 - Crie uma classe chamada Pessoa que tenha os atributos nome e idade. 
# Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)

print(f"Pessoa 1: Nome - {p1.nome}, Idade - {p1.idade}")
print(f"Pessoa 2: Nome - {p2.nome}, Idade - {p2.idade}")