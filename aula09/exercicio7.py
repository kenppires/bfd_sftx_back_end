# 7. Crie uma função chamada `dados_pessoais` que receba informações de uma pessoa 
# (nome, idade, cidade, etc.) usando `**kwargs` e imprima cada dado em uma linha.
#    Exemplo de chamada:

#    ```python
#    dados_pessoais(nome="Ana", idade=25, cidade="Recife")
#    ```

def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")
print("---")
dados_pessoais(nome="João", idade=30, cidade="São Paulo", profissao="Engenheiro")