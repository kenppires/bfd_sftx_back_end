#6 - Contando frequência de palavras
#Escreva uma função que receba uma lista de palavras e retorne um 
#dicionário com a contagem de cada palavra.
#
#      palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def contar_frequencia(lista_de_palavras):
    frequencia = {}
    for palavra in lista_de_palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia

contagem_palavras = contar_frequencia(palavras)

print(contagem_palavras)