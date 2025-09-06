# 8. Crie uma função chamada `calculadora` que tenha dentro dela outras funções (`somar`, `subtrair`, `multiplicar`, `dividir`).
#    A função principal deve permitir escolher a operação e retornar o resultado.

def calculadora(operacao, a, b):
    def somar(x, y): return x + y
    def subtrair(x, y): return x - y
    def multiplicar(x, y): return x * y
    def dividir(x, y): return x / y if y != 0 else "Erro: divisão por zero!"

    operacoes = {
        "somar": somar,
        "subtrair": subtrair,
        "multiplicar": multiplicar,
        "dividir": dividir
    }

    return operacoes.get(operacao, lambda x, y: "Operação inválida!")(a, b)

print(calculadora("somar", 10, 5))
print(calculadora("subtrair", 10, 5))
print(calculadora("multiplicar", 10, 5))
print(calculadora("dividir", 10, 5))
print(calculadora("dividir", 10, 0))
print(calculadora("potencia", 10, 2))