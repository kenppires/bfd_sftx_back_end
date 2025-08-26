# 2 - Usando o dicionário abaixo, use o método .get() para obter o valor da chave "telefone", 
# retornando "Não informado" se a chave não existir.

# cliente = {"nome": "Amanda", "idade": 31}


cliente = {"nome": "Amanda", "idade": 31}

chave = "telefone"

if cliente.get(chave):
    print(f"a chave ",{chave},"se encontra no banco de dados!")
else:
    print("Não encontrado!")