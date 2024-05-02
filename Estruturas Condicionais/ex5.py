# EX 5
"""
    Faça um algoritmo que solicita um número inteiro e exibe uma mensagem indicando se ele é positivo,
    negativo ou zero.   
"""
num = int(input("Digite um número inteiro: "))

if num < 0:
    print("É Negativo!")
elif num > 0:
    print("É Positivo")
else:
    print("É zero")
