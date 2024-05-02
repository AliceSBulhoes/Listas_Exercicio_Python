# EX 9
"""
    Faça um algoritmo que solicita ao usuário três valores correspondentes aos lados de um triângulo.
    Informe se o triângulo é equilátero (possui 3 lados iguais), isósceles (possui dois lados iguais) ou
    escaleno (não possui lados iguais).
"""
num = float(input("Digite um dos lados do triangulo: "))
num2 = float(input("Digite outro lado do triangulo: "))
num3 = float(input("Digite outro lado do triangulo: "))

if num2 == num3 == num:
    print("É um triângulo equilátero")
elif num2 == num3 or num2 == num or num == num3:
    print("É um triângulo isósceles")
else:
    print("É um triângulo escaleno")