# 4. Implemente um programa que abra um arquivo chamado `dados.txt` (não precisa existir). Use `try` e `finally` para 
# garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

import os

def abrir_arquivo():
    nome_arquivo = "dados.txt"
    arquivo = None

    try:
        arquivo = open(nome_arquivo, "r")
        conteudo = arquivo.read()
        print(f"Conteúdo do arquivo:\n{conteudo}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        print("\nEncerrando programa...")
        if arquivo:
            arquivo.close()
            print("O arquivo fechado com sucesso.")

abrir_arquivo()