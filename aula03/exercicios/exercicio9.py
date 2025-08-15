def calculadora():
    print("#Calculadora#")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

escolha = input("Escolha a operação (1/2/3/4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == "1":
    print(f"{num1} + {num2} = {num1+num2}")
elif escolha == "2":
    print(f"{num1}-{num2} = {num1-num2}")
elif escolha == "3":
    print(f"{num1}x{num2} = {num1*num2}")
elif escolha == "4":
    if num2 != 0:
        print(f"{num1}/{num2} = {num1/num2}")
    else:
        print("Erro: Divisão por zero!")
else:
    print("Erro: Opção Inválida")

calculadora()
