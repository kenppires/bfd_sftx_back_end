# 5. Crie uma função `dividir(a, b)` que lance (`raise`) uma exceção `ZeroDivisionError` se `b` for igual a zero. 
# Caso contrário, retorne o resultado da divisão.

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Não é possível dividir por zero.")
    return a / b


try:
    resultado = dividir(10, 2)
    print(f"10 dividido por 2 é igual a {resultado}")
except ZeroDivisionError as erro:
    print(erro)

try:
    resultado = dividir(5, 0)
    print(f"5 dividido por 0 é igual a {resultado}")
except ZeroDivisionError as erro:
    print(erro)