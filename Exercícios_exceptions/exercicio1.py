# 1. Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

def obter_numero_inteiro():
    while True:
        try:
            entrada = input("Digite um número inteiro: ")
            numero = int(entrada)
            print(f"O número inteiro que você digitou é: {numero}")
            
        except ValueError:
            print(f"Entrada inválida. '{entrada}' Não um número inteiro.")
        break

numero = obter_numero_inteiro()