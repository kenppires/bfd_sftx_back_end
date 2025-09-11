# 9. Crie uma função `sacar(saldo, valor)` que:

# * Lance (`raise`) uma exceção personalizada `SaldoInsuficienteError` se o valor for maior que o saldo.
# * Caso contrário, retorne o novo saldo.
#   Teste a função dentro de um `try-except` e exiba uma mensagem apropriada ao usuário.

class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Saldo insuficiente para realizar a operação."):
        super().__init__(mensagem)

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente. O valor solicitado é maior que o saldo disponível.")
    
    novo_saldo = saldo - valor
    return novo_saldo

saldo_inicial = 500.00
valor_saque_sucesso = 200.00
valor_saque_falha = 700.00

print(f"Saldo inicial: R$ {saldo_inicial:.2f}")
try:
    novo_saldo = sacar(saldo_inicial, valor_saque_sucesso)
    print(f"Saque de R$ {valor_saque_sucesso:.2f} realizado com sucesso!")
    print(f"Novo saldo: R$ {novo_saldo:.2f}")
except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")

print("-" * 30)


print(f"Saldo inicial: R$ {saldo_inicial:.2f}")
try:
    novo_saldo = sacar(saldo_inicial, valor_saque_falha)
    print(f"Saque de R$ {valor_saque_falha:.2f} realizado com sucesso!")
    print(f"Novo saldo: R$ {novo_saldo:.2f}")
except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")