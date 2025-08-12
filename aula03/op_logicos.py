idade = int(input("Qual a sua idade?: "))
carteira = input("Tem carteira de motorista?(sim/nao): ")
alcool = input("Ingeriu bebida alcoolica?(sim/nao): ")

if idade := 18 and carteira == "sim" and alcool == "nao":
    print("apto a dirigir!")
else:
    print("Não esta apto a dirigir!")