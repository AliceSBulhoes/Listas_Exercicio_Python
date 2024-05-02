# Ex 10

"""
    Faça um programa que solicita ao usuário um único número inteiro com três dígitos e exibe o
    número invertido.
        Exemplo:
        Informe um número com 3 dígitos: 136
        Número invertido: 631
"""
info = int(input("Digite um número inteiro com 3 dígitos: "))

num1 = info%10
num2 = (info%100 - (info%10))//10
num3 = info//100

print(f"{num1}{num2}{num3}")
