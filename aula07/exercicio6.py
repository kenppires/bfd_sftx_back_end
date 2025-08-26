# 6 - Crie um dicionário compras com pelo menos 3 itens (nome do produto como
# chave e preço como valor). Em seguida, use .values() para calcular o total da compra.

compras = {"Monitor":1400, "Gabinete":350, "Teclado":400}

total = 0

for valor in compras.values():
    total += valor
    
# total = sum(compras.values())
print(f"Total das compras: R${total}")
