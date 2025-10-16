#3 - Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
# Departamento deve agregar funcionários já criados.

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"Funcionário: {self.nome} ({self.cargo})"

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.funcionarios.append(funcionario)
            print(f"'{funcionario.nome}' adicionado ao Departamento '{self.nome}'.")

    def listar_funcionarios(self):
        print(f"\n### Funcionários do Departamento '{self.nome}' ###")
        if self.funcionarios:
            for func in self.funcionarios:
                print(f"- {func}")
        else:
            print("Nenhum funcionário neste departamento.")

func1 = Funcionario("Maria Santos", "Gerente")
func2 = Funcionario("Pedro Lima", "Analista Jr.")

depto_ti = Departamento("Tecnologia da Informação")

depto_ti.adicionar_funcionario(func1)
depto_ti.adicionar_funcionario(func2)

depto_ti.listar_funcionarios()