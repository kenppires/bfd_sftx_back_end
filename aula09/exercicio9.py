# 9. Crie uma função chamada `aplicar_operacao` que receba dois números e uma função como parâmetros.
#     A função deve aplicar a operação recebida (ex: soma, multiplicação).
#     Exemplo:

#     ```python
#     def soma(a, b): return a + b
#     aplicar_operacao(3, 4, soma)  # deve retornar 7
#     ```

def aplicar_operacao(a, b, funcao):
    return funcao(a, b)


def soma(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

print(aplicar_operacao(3, 4, soma))
print(aplicar_operacao(3, 4, multiplicar))