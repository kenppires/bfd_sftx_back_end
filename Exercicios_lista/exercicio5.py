#Questão 5: Remover um livro da lista

livros = ["Drácula", "A Metamorfose", "O Senhor dos Anéis"]

livro = "Silêncio dos Inocentes"
if livro in livros:
    livros.remove(livro)
    print("Livro removido com sucesso")
    print(livros)
else:
    print("livro não encontrado")