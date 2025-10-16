#5 - Crie a classe Carro que possui um Motor. 
# O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, 
# o Motor também deixa. Mostre isso criando e depois apagando o objeto.

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        print(f"Motor {self.potencia}cc CRIADO.")

    def __del__(self):
        print(f"Motor {self.potencia}cc não existe.")

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)
        print(f"Carro {self.modelo} CRIADO com sucesso.")

    def __del__(self):
        print(f"Carro {self.modelo} Não existe.")
        if hasattr(self, 'motor'):
            del self.motor
            print(f"-> A referência ao Motor foi removida.")


print("--- Início da Criação ---")
meu_carro = Carro("Ford Fusion", 2000)

print("\n--- Início da Exclusão ---")
del meu_carro