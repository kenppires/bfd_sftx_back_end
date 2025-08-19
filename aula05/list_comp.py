lista1 = []
for i in range(10):
    lista1.append(i*2)

print(lista1)

#lista2 = [i for i in range(10) if i%2==0]
#print(lista2)

lista2 = [[linha for linha in range(3)] for coluna in range(3)]
print(lista2)