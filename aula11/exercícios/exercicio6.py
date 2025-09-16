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
            return True
        else:
            return False

conta = ContaBancaria("José",1000)

if conta.sacar(200):
    print(f"Saque concluído \n>Saldo atual: R${conta.saldo}")
else:
    print(f"Não foi possível realizar o saque. \n>Saldo Insuficiente.") 

if conta.sacar(3000):
    print(f"Saque concluído \n>Saldo atual: R${conta.saldo}")
else:
    print(f"Não foi possível realizar o saque. \n>Saldo Insuficiente.")