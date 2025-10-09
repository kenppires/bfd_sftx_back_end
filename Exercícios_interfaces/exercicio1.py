#1 - Criando uma interface
#Crie uma interface chamada Pagamento com um método abstrato processar(valor). 
# Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. 
#  Mostre como chamar processar() para cada uma.

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"o valor de R${valor} foi pago no Cartão de Crédito!"

class Boleto(Pagamento):
    def processar(self, valor):
        return f"o valor de R${valor} foi pago no Boleto!"
    
cliente1 = CartaoCredito()
cliente2 = Boleto()

print(cliente1.processar(500))
print(40*"-")
print(cliente2.processar(300))