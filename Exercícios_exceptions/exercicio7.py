# 7. Peça ao usuário dois números e divida o primeiro pelo segundo. Trate **dois tipos de erro**:

# * `ValueError` se o usuário digitar algo inválido
# * `ZeroDivisionError` se tentar dividir por zero

def dividir_numeros():
    try:
        entrada1 = input("Digite o numerador: ")
        numerador = float(entrada1)

        entrada2 = input("Digite o denominador: ")
        denominador = float(entrada2)

        resultado = numerador / denominador
        print(f"O resultado da divisão é: {resultado}")

    except ValueError:
        print("\nErro: Entrada inválida. Digite apenas números.")
    
    except ZeroDivisionError:
        print("\nErro: Não é possível dividir por zero.")

dividir_numeros()