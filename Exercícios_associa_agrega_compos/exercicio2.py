#2 - Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

class Onibus:
    def __init__(self, placa, linha):
        self.placa = placa
        self.linha = linha

    def get_informacao(self):
        return f"Ônibus da linha {self.linha} (Placa: {self.placa})"

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    # Método em Aluno que usa a classe Onibus
    def ir_para_universidade(self, onibus):
        if isinstance(onibus, Onibus):
            info_onibus = onibus.get_informacao()
            print(f"{self.nome} (Matrícula: {self.matricula}) está pegando o {info_onibus} para a universidade.")
        else:
            print(f"{self.nome} está indo de outra forma.")

onibus_azul = Onibus("ABC-1234", "42 - Campus Leste")
aluno_joao = Aluno("João Silva", "2023001")

aluno_joao.ir_para_universidade(onibus_azul)