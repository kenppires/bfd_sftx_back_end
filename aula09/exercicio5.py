# 5. Crie uma função chamada `operacoes` que receba dois números e retorne **a soma, a subtração e a multiplicação** deles.

def operacoes(num1, num2):
    return f"Soma: {num1}+{num2}={num1+num2} ",f"Subtração: {num1}-{num2}={num1-num2} ",f"Mutiplicação: {num1}*{num2}={num1*num2}"

print(operacoes(5,2))