# 2. Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

def multiplicar_numeros():
    try:
        entrada1 = input("Digite o primeiro número: ")
        numero1 = float(entrada1)

        entrada2 = input("Digite o segundo número: ")
        numero2 = float(entrada2)

        resultado = numero1 * numero2
        print(f"Resultado da multiplicação: {resultado}")

    except ValueError:
        print(f"Erro: Não é um número válido. ")

multiplicar_numeros()