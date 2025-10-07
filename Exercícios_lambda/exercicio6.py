#6 - Produto dos números (reduce + lambda)
# Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].

from functools import reduce

numeros = [2, 3, 4, 5]

produto_total = reduce(lambda x, y: x * y, numeros)

print(f"Lista original: {numeros}")
print(f"Produto total dos números: {produto_total}")