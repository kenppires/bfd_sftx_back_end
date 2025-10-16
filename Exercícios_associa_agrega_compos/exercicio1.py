#1 - Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.titulo} (Autor: {self.autor})"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        # Associação: Pessoa tem uma lista de referências para objetos Livro
        self.livros_favoritos = []

    def adicionar_livro_favorito(self, livro):
        if isinstance(livro, Livro):
            self.livros_favoritos.append(livro)
            print(f"{self.nome} adicionou '{livro.titulo}' à lista de favoritos.")

    def mostrar_favoritos(self):
        print(f"\nLivros favoritos de {self.nome}:")
        if self.livros_favoritos:
            for livro in self.livros_favoritos:
                print(f"- {livro}")
        else:
            print("(Nenhum favorito.)")

livro1 = Livro("A Bússola de Ouro", "Philip Pullman")
livro2 = Livro("1984", "George Orwell")

pessoa1 = Pessoa("Alice")

pessoa1.adicionar_livro_favorito(livro1)
pessoa1.adicionar_livro_favorito(livro2)
pessoa1.mostrar_favoritos()