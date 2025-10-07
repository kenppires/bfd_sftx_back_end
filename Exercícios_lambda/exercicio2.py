#2 - Filtrar pares (filter + lambda)
# Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.

numeros = [10, 15, 20, 25, 30]


pares_filter_obj = filter(lambda x: x % 2 == 0, numeros)

pares = list(pares_filter_obj)

print(f"Lista original: {numeros}")
print(f"Números pares: {pares}")