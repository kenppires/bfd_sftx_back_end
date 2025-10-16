#6 - Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). 
# Cada Comodo deve ser criado dentro da Casa.

class Comodo:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area
        print(f"  -> Cômodo '{self.nome}' ({self.area}m²) criado.")

    def __str__(self):
        return f"Cômodo: {self.nome} ({self.area}m²)"

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        print(f"\nCASA no endereço '{self.endereco}' está sendo construída...")

        self.sala = Comodo("Sala de Estar", 30)
        self.cozinha = Comodo("Cozinha", 15)
        self.quarto_principal = Comodo("Quarto Principal", 18)
        self.comodos = [self.sala, self.cozinha, self.quarto_principal]

    def listar_comodos(self):
        print(f"\nLista de Cômodos da Casa em {self.endereco}:")
        for comodo in self.comodos:
            print(f"- {comodo}")

minha_casa = Casa("Rua das Palmeiras, 100")
minha_casa.listar_comodos()