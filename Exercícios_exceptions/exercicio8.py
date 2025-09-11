# 8. Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:

# * `try` para a conversão,
# * `else` para verificar se é par ou ímpar,
# * `finally` para exibir "Fim do programa".

def verificar_par():
    try:
        entrada = input("Digite um número inteiro: ")
        numero = int(entrada)
    except ValueError:
        print("Erro: Entrada inválida. Não é um número inteiro.")
    else:
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    finally:
        print("\nFim do programa.")

verificar_par()