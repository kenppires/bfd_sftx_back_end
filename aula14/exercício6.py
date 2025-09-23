#6. Crie uma classe `Autenticacao` com um método `login()`. Crie outra classe 
# `Permissao` com um método `verificar_permissao()`. Em seguida, crie uma classe 
# `Administrador` que herda de ambas. Como usar os métodos herdados?

class Autenticacao:
    def login(self):
        print("-> Usuário autenticado com sucesso.")
        return True

class Permissao:
    def verificar_permissao(self, nivel):
        print(f"-> [PERMISSÃO]: Verificando nível de acesso '{nivel}'...")
        if nivel == "admin":
            return True
        else:
            return False

class Administrador(Autenticacao, Permissao):
    def __init__(self, nome, acesso):
        self.nome = nome
        self.acesso = acesso
        print(f"\nAdministrador criado: {self.nome} (Nível: {self.acesso})")

    def executar(self):
        if self.login():
            if self.verificar_permissao("admin"):
                print(f"-> [ADMIN]: {self.nome} executou a tarefa com sucesso!")
            else:
                print(f"-> [ADMIN]: Falha na permissão. Tarefa bloqueada.")
        else:
            print("-> [ADMIN]: Não autenticado. Tarefa bloqueada.")

admin1 = Administrador("Lucas", "admin")

print("\n--- Executando Tarefa ---")
admin1.executar()

print("\n--- Chamada Direta dos Métodos Herdados ---")
autenticado = admin1.login() # Método de Autenticacao
autorizado = admin1.verificar_permissao(admin1.acesso) # Método de Permissao
print(f"Resultado da Verificação: {autorizado}")