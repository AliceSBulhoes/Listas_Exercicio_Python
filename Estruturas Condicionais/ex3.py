# EX3
"""
    Faça um algoritmo que solicita ao usuário um número inteiro e exiba este número na tela. Se o
    número for negativo, antes de ser exibido, ele deve ser transformado no equivalente positivo
"""
num = int(input("Digite um número inteiro: "))


if num > 0:
    print(f'O número escrito é {num}')
else:
    num1 = num*-1
    print(f'O número escrito é {num1}')
