#2 - Crie uma classe 'Pessoa' que tenha os atributos: nome, data de nascimento, cpf e identidade.
#Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters.

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf

    def get_id(self):
        return self.__identidade

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
        print("CPF atualizado com sucesso.\n")

    def set_id(self, nova_identidade):
        self.__identidade = nova_identidade
        print("Identidade atualizada com sucesso.\n")

pessoa1 = Pessoa("Maria", "10/05/1990", "123.456.789-00", "MG-12.345.678")

print(40*"-")
print(f"Nome: {pessoa1.nome}")
print(f"Data de Nascimento: {pessoa1.data_nascimento}")
print(f"CPF: {pessoa1.get_cpf()}") #get
print(f"Identidade: {pessoa1.get_id()}") #get
print(40*"-")

pessoa1.set_cpf("987.654.321-01") #set
pessoa1.set_id("SP-98.765.432") #set

print(40*"-")
print(f"Nome: {pessoa1.nome}")
print(f"Data de Nascimento: {pessoa1.data_nascimento}")
print(f"CPF*: {pessoa1.get_cpf()}")
print(f"Identidade*: {pessoa1.get_id()}")
print(40*"-")