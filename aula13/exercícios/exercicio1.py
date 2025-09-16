#1 - Criar a classe "Pessoa" com suas características e a classe "Funcionáro" que herde Pessoa.

class Pessoa:
    def __init__(self,nome,idade,rg,cpf):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.cpf = cpf

class Funcionario(Pessoa):
    ...

pessoa1 = Funcionario("João", 23, "8392881", "918.283.123.42")
pessoa2 = Funcionario("Maria", 20, "6854987", "587.254.154.58")

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.rg)
print(pessoa1.cpf)
print(40*"-")

print(pessoa2.nome)
print(pessoa2.idade)
print(pessoa2.rg)
print(pessoa2.cpf)