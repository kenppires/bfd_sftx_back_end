#4. Na classe `Cliente`, adicione o atributo `saldo`. Adicione um método construtor 
# em `Cliente` que inicialize também os atributos de `Usuario` usando `super()`.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"-INFORMAÇÕES DE USUÁRIO-")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")

    def saudacao(self):
        return f"Olá, usuário"
    
    def __str__(self):
        return (f"Nome: {self.nome}\nEmail:{self.email}")

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

    def saudacao(self):
        return f"Olá, Cliente"   
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Saldo: R${self.saldo:.2f}")

    
usuario1 = Usuario("Ana", "ana@usuario.com")
cliente1 = Cliente("Bruno", "bruno@cliente.com", 2000.50)

print("-" * 30)
print(f"Dados do cliente: ")
cliente1.exibir_informacoes()

print("-" * 30)
print(f"Acesso ao Saldo: R${cliente1.saldo:.2f}")
print(f"Acesso ao Email: {cliente1.email}")
print("-" * 30)