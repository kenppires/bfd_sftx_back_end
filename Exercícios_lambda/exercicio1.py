# 1 - Dobro dos números (map + lambda)
# Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.

numeros = [1, 2, 3, 4, 5]

dobros_map_obj = map(lambda x: x * 2, numeros)


dobros = list(dobros_map_obj)

print(f"Lista original: {numeros}")
print(f"Lista com o dobro dos números: {dobros}")