# 3. Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco `else`.

def converter_num():
    try:
        entrada = input("Digite um número inteiro: ")
        numero = int(entrada)
    except ValueError:
        print("Erro: Não é um número inteiro válido.")
    else:
        print(f"Número inteiro digitado: {numero}")

converter_num()