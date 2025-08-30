#10 - Ordenando dicionário por valor
#Dado o dicionário:
#   pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
#Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

# Cria uma cópia do dicionário para não modificar o original
copia_pontuacoes = list(pontuacoes.items())
pontuacoes_ordenadas = []

# Encontra o item com a maior pontuação e o move para a lista ordenada
while copia_pontuacoes:
    maior_pontuacao = -1
    item_maior_pontuacao = None
    
    # Encontra o item com a maior pontuação na lista
    for item in copia_pontuacoes:
        nome, pontuacao = item
        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            item_maior_pontuacao = item
            
    # Adiciona o item à lista de ordenados e o remove da lista temporária
    pontuacoes_ordenadas.append(item_maior_pontuacao)
    copia_pontuacoes.remove(item_maior_pontuacao)

for nome, pontuacao in pontuacoes_ordenadas:
    print(f"{nome}: {pontuacao}")