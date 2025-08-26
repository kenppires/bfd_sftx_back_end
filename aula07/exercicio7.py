#7 - Dado o dicionário:

# frutas = {"maçã": 3, "banana": 5, "laranja": 2}
# Imprima as frutas que têm mais de 2 unidades usando um laço for.

frutas = {"maçã": 3, "banana": 5, "laranja": 2}

for fruta, qtd in frutas.items():
    if qtd > 2:
        print(fruta)