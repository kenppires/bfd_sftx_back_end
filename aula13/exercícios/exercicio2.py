#2 - Você tem uma empresa que usa computadores padronizados, contudo o departamento de IA precisa de uma placa de vídeo. 
#  Crie a classe "Computador" que tenha modelo, processador, quantidade de memória e departamento como atributos e crie 
# uma classe que herda as características da classe computador, mas adicionando a placa de vídeo.

class Computador:
    def __init__(self,modelo,processador,ram,departamento):
        self.modelo = modelo
        self.processador = processador
        self.ram = ram
        self.departamento = departamento
    
    def __str__(self):
        return (f"Modelo: {self.modelo}\n"
                f"Processador: {self.processador}\n"
                f"Memória RAM: {self.ram}\n"
                f"Departamento: {self.departamento}")


class ComputadorGamer(Computador):
    def __init__(self, modelo, processador, ram, departamento, gpu):
        super().__init__(modelo, processador, ram, departamento)
        self.gpu = gpu
    
    def __str__(self):
        pcbasic = super().__str__()
        return f"{pcbasic}\nGPU: {self.gpu}"
    

pc1 = ComputadorGamer("Dell","Intel","32GB DDR4 6400Mhz","Informática","Geforce")

pc2 = Computador("Alienware", "AMD", "64GB DDR5 5200Mhz", "Marketing")

print(pc1)
print(40*"-")

print(pc2)