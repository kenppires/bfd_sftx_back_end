#2. Implemente um método `exibir_informacoes()` na classe `Usuario` e herde esse método 
# em `Cliente`. Mostre como chamar o método herdado a partir de um objeto `Cliente`.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"-INFORMAÇÕES DE USUÁRIO-")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
    
    def __str__(self):
        return (f"Nome: {self.nome}\nEmail:{self.email}")

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
    
    def __str__(self):
        return super().__str__()
    
cliente1 = Cliente("Carla Silva", "carlasilva@exemplo.com")

cliente1.exibir_informacoes()