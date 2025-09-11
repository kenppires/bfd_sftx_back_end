#5 - Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o 
# saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito realizado. \n>Novo Saldo:{self.saldo:.2f}")
        print(40*"-")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque realizado. \n>Novo Saldo:{self.saldo:.2f}")
            print(40*"-")
        else:
            print("Saldo insuficiente!")
            print(40*"-")


conta = ContaBancaria("José",500)
conta.depositar(200)
conta.sacar(600)
conta.sacar(1000)