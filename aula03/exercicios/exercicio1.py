#Retorna se o número digitado pelo usuário é ímpar ou par

num = float(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número {num} é Par!")
else:
    print(f"O número {num} é Ímpar!")