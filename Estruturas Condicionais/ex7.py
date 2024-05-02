# EX 7
"""
    Faça um algoritmo que solicite dois números ao usuário e exiba apenas o maior deles. Caso eles sejam
    iguais exiba a mensagem “Números Iguais”.
"""
num = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num > num2:
    print(num)
elif num2 > num:
    print(num2)
elif num == num2:
    print("Os números são iguais")