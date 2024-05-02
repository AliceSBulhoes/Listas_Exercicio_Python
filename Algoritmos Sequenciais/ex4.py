# Ex 4
"""
    Escreva um algoritmo que solicite a temperatura em graus Celsius e a converta para Fahrenheit.
    Utilize a fórmula abaixo:
                                             F = C * 1.8 + 32
"""
temp = int(input("Digite a temperatura em C°: "))

far = temp*1.8 +32

print(f"A temperatura que você estaria se estivesse no EUA seria {far} F")
