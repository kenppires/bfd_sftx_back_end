#7 - Ordenar por último caractere (sorted + lambda)
# Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.

frutas = ["banana", "uva", "maçã", "laranja"]

frutas_ordenadas = sorted(frutas, key=lambda x: x[-1])

print(f"Lista original: {frutas}")
print(f"Lista ordenada pelo último caractere: {frutas_ordenadas}")