# 6. Crie uma função chamada `media` que receba uma quantidade variável de números e retorne a média deles.
#    Teste com 3, 5 e 7 valores diferentes.

def media(*numeros):
    if len(numeros) == 0:
        return 0
    soma = sum(numeros)
    return soma / len(numeros)

print("Média de 3 valores:", media(2, 4, 6))  
print("Média de 5 valores:", media(10, 20, 30, 40, 50))  
print("Média de 7 valores:", media(3, 6, 9, 12, 15, 18, 21))  
