#1 - Crie uma classe chamada Pessoa que tenha os atributos nome e idade. 
# Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

class Pessoa:
    nome = "João Bezerra"
    idade = 83

joao = (f"Nome: {Pessoa.nome}", f"Idade: {Pessoa.idade}")
print(joao)