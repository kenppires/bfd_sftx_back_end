#1. Crie uma classe `Usuario` com atributos `nome` e `email`. 
# Depois, crie uma classe `Cliente` que herde de `Usuario`. 
# Crie uma instancia de um cliente e acesse todos os atributos.

class Usuario:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return (f"Nome: {self.nome}\nEmail:{self.email}")

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def __str__(self):
       return super().__str__()
    
cliente1 = Cliente("João", "joaoc@gmail.com")


print(cliente1)


