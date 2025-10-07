#5 - Primeira letra maiúscula (map + lambda)
# Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

nomes = ["ana", "pedro", "maria"]

nomes_map_object = map(lambda x: x.capitalize(), nomes)

# Convertendo o objeto map em uma lista para visualização
nomes_maisc = list(nomes_map_object)

print(f"Lista original: {nomes}")
print(f"Lista com nomes com primeira letra em maiúsculo: {nomes_maisc}")