soma = 0

while True:
    x = int(input(f"informe um numero(0 para parar): "))
    if x == 0:
        break
    soma += x
    print(f"\n Total: {soma} \n")
print(f"Soma dos números digitados: {soma}")

