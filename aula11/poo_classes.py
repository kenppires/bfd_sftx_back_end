#adicionando atributos
class Cachorro:
    especie = "Canis lupus familiaris"
    nome = "Toto"
    raca = "caramelo"
    idade = 2

#instanciando obj
auau = Cachorro()
print(auau)    

#acessando atributos
print(auau.especie, auau.nome, auau.raca, auau.idade, sep="\n")

#atributos de objeto
class Cachorro:
    especie = "Canis lupus familiaris"
    def __init__(self, nome, raca, idade): #Método Construtor
        self.nome = nome 
        self.raca = raca
        self.idade = idade

doguinho01 = Cachorro("Rex", "Caramelo", 2)
# print(doguinho01)
# print(doguinho01.especie, doguinho01.nome, doguinho01.raca, doguinho01.idade, sep="\n")

#metodo especial __str__
def __str__(self):
    return f"especie: {self.especie}\nRaça: {self.raca}\nIdade: {self.idade}"


class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.operacoes = []

    def __str__(self):
        return f"Conta nº {self.numero_conta} do titular {self.nome} com saldo R${self.saldo}"
    
    def registro_operacoes():
    
        def saque(self, valor):
            if valor > self.saldo:
                print("Saldo insuficiente")
            else:
                self.saldo -= valor
                self.operacoes.append(["saque", valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["saque", valor])

    def extrato(self):
        for operacao in self.operacoes:
            print(operacao)

    

conta1 = ContaBancaria("Test",11111,3000)

print(conta1)
