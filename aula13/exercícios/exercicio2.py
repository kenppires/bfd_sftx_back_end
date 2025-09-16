#2 - Você tem uma empresa que usa computadores padronizados, contudo o departamento de IA precisa de uma placa de vídeo. 
#  Crie a classe "Computador" que tenha modelo, processador, quantidade de memória e departamento como atributos e crie 
# uma classe que herda as características da classe computador, mas adicionando a placa de vídeo.

class Computador:
    def __init__(self,modelo,processador,memoria,departamento):
        self.modelo = modelo
        self.processador = processador
        self.memoria = memoria
        self.departamento = departamento


class ComputadorGamer(Computador):
    ...

pc1 = ComputadorGamer("Dell","Intel","32GB DDR4 6400Mhz","Informática","Geforce")

print(pc1.gpu)

-