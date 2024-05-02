# EX 8
"""
    Faça um algoritmo que solicita ao usuário três números e exibe na tela apenas o menor deles, ou uma
    mensagem informando que os números são iguais.
"""
num = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

if num > num3 and num2 > num3:
    print(num3)
elif num2 > num and num3 > num:
    print(num)
elif num > num2 and num3 > num2:
    print(num2)
elif num == num2 == num3:
    print("Os números são iguais")