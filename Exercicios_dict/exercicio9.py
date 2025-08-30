#9 - Mesclando dois dicionários
#Escreva uma função que recebe dois dicionários e retorna um novo 
#dicionário contendo todos os pares chave-valor. Se houver chaves 
#repetidas, o valor do segundo dicionário deve prevalecer.

def mesclar_dicionarios(dic1, dic2):
    dic_mesclado = dic1.copy()
    dic_mesclado.update(dic2)
    return dic_mesclado

dicionario1 = {"a": 1, "b": 2, "c": 7}
dicionario2 = {"c": 3, "d": 4}

dicionario = mesclar_dicionarios(dicionario1, dicionario2)

print(dicionario)