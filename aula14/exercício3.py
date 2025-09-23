#3. Na classe `Usuario`, crie um método `saudacao()` que retorna `"Olá, usuário"`. 
# Na classe `Cliente`, sobrescreva esse método para retornar `"Olá, cliente"`. Mostre como funciona a chamada.

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
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def saudacao(self):
        return f"Olá, Cliente"   
    
    def __str__(self):
        return super().__str__()

    
usuario1 = Usuario("Ana", "ana@usuario.com")
cliente1 = Cliente("Bruno", "bruno@cliente.com")

print("-" * 30)
saudacao_usuario = usuario1.saudacao()
print(f" Usuario: {saudacao_usuario} {usuario1.nome}")

print("-" * 30)
saudacao_cliente = cliente1.saudacao()
print(f"Cliente: {saudacao_cliente} {cliente1.nome}") # Retorna "Olá, cliente"
print("-" * 30)