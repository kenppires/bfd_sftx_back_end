#4 - Adicione uma nova chave chamada "disponível" ao dicionário com o valor True.
#livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}

livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}

livro.update({"disponível": True})

print(livro)