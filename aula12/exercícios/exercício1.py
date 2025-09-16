#1 - Na classe 'ContaBancaria', converta 'saldo' para atributo privado. 
# Crie um método setter e um getter para acessar e modificar esse atributo.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo #atributo privado

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
            print(f"Saldo atualizado para R${self.__saldo}\n")
        else:
            print("Erro: O saldo não pode ser negativo.\n")


conta = ContaBancaria("João")

print(f"Saldo inicial: R${conta.get_saldo()}\n")

conta.set_saldo(500)
conta.set_saldo(-100)

print(f"Saldo após as tentativas: R${conta.get_saldo()}\n")