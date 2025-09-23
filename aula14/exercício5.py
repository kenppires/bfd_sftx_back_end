#5. Crie uma classe `Funcionario` que herda de `Usuario` e, em seguida, crie uma classe `Gerente` 
# que herda de `Funcionario`. Mostre como instanciar um gerente e acessar seus atributos.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def saudacao(self):
        return f"Olá, usuário {self.nome}"

class Funcionario(Usuario):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula
    
    def saudacao(self):
        return f"Olá, funcionário {self.nome} (Matrícula: {self.matricula})"

class Gerente(Funcionario):
    def __init__(self, nome, email, matricula, setor):
        super().__init__(nome, email, matricula)
        self.setor = setor
    
    def saudacao(self):
        return f"Olá, gerente {self.nome} do setor de {self.setor}"


gerente1 = Gerente(
    nome="Carlos Souza",
    email="carlos@empresa.com",
    matricula="G1024",
    setor="TI"
)

print(f"Saudação: {gerente1.saudacao()}")
print("-" * 40)
print(f"Nome (de Usuario): {gerente1.nome}")
print(f"Email (de Usuario): {gerente1.email}")
print(f"Matrícula (de Funcionario): {gerente1.matricula}")
print(f"Setor (de Gerente): {gerente1.setor}")
print("-" * 40)