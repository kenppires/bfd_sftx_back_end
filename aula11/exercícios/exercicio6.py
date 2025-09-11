#6 - Modifique a classe ContaBancaria para que o método sacar retorne 
# True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
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
            return True
        else:
            print("Saldo insuficiente!")
            print(40*"-")
            return False


conta = ContaBancaria("José",1000)
conta.depositar(500)

if conta.sacar(200):
    print(f"Saque concluído")
else:
    print(f"Não foi possível realizar o saque.") 

if conta.sacar(3000):
    print(f"Saque concluído")
else:
    print(f"Não foi possível realizar o saque. \nSaldo:{conta.saldo}") 