#8 - Verifique se a chave "senha" está presente no dicionário abaixo. 
# Se não estiver, adicione-a com o valor "123456".

# usuario = {"login": "joaosilva"}

usuario = {"login": "joaosilva"}


if "senha" in usuario:
    print(usuario)
else:
    usuario["senha"] = "123456"
    print(usuario)
