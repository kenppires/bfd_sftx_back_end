#3 - Soma dos números (reduce + lambda)
# Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].

from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma_total = reduce(lambda x, y: x + y, numeros)

print(f"Lista original: {numeros}")
print(f"Soma total dos números: {soma_total}")