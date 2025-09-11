# 6. Crie uma exceção personalizada chamada `IdadeInvalidaError`. Depois, crie uma função `cadastrar_idade(idade)` 
# que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError(f"A idade não pode ser negativa, você digitou: {idade}")
    
    print(f"Idade {idade} cadastrada com sucesso.")

try:
    cadastrar_idade(25)
except IdadeInvalidaError as erro:
    print(f"Ocorreu um erro: {erro}")

print("-" * 20)

try:
    cadastrar_idade(-10)
except IdadeInvalidaError as erro:
    print(f"Ocorreu um erro: {erro}")