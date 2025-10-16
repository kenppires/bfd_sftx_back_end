#4 - Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, 
# enquanto Time agrega jogadores em uma lista.

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"Jogador: {self.nome} ({self.posicao})"

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.elenco = []

    def contratar_jogador(self, jogador):
        if isinstance(jogador, Jogador):
            self.elenco.append(jogador)
            print(f"O jogador {jogador.nome} foi contratado pelo {self.nome}.")

    def listar_elenco(self):
        print(f"\nElenco do {self.nome}:")
        if self.elenco:
            for jogador in self.elenco:
                print(f"- {jogador}")
        else:
            print("Time sem jogadores.")

jogador_a = Jogador("Ronaldo", "Atacante")
jogador_b = Jogador("Cafu", "Lateral-Direito")

time_criciuma = Time("Criciúma Esporte Clube")
time_criciuma.contratar_jogador(jogador_a)
time_criciuma.contratar_jogador(jogador_b)

time_criciuma.listar_elenco()