# EX 6
"""
    Faça um algoritmo que solicita ao usuário dois números inteiros. O primeiro é o valor das horas e o
    segundo dos minutos. Verifique se a hora é válida ou inválida e exiba uma mensagem correspondente
    (São válidas as horas entre 00:00 e 23:59).
"""
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))


if 0<=num1<24 and 0<=num2<60:
    print(f"São {num1:02}:{num2:02}")
else:
    print("São válidas as horas entree 00:00 e 23:59")

