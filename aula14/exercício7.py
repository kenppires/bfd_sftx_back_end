#7. Usando o exemplo anterior, adicione um método `status()` em `Autenticacao` e 
# também em `Permissao`. Se a classe `Administrador` herda das duas, qual versão 
# de `status()` será chamada? Use `Administrador.__mro__` para mostrar a ordem.

class Autenticacao:
    def login(self):
        print("-> [A] Usuário autenticado.")
        return True

    def status(self):
        return "Autenticação Ativa"

class Permissao:
    def verificar_permissao(self, nivel):
        print(f"-> [P] Verificando nível de acesso '{nivel}'...")
        return nivel == "admin"
    
    def status(self):
        return "Permissão Ativa"

class Administrador(Autenticacao, Permissao):
    def __init__(self, nome, acesso):
        self.nome = nome
        self.acesso = acesso

admin1 = Administrador("Helena", "admin")

chamada_status = admin1.status()
print(f"Chamando admin1.status(): {chamada_status}")
print("-" * 50)

print("Ordem de Resolução de Métodos (MRO):")
print(Administrador.__mro__)