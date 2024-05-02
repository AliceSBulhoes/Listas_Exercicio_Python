# EX2
"""
    Faça um algoritmo que solicita ao usuário um valor inteiro e exibe uma mensagem informando se o
    número é par ou ímpar.
"""
num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')
