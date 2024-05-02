# Ex 5
"""
    Escreva um algoritmo que solicite o peso e a altura de uma pessoa e calcule o seu IMC (Índice de
    Massa Corpórea). Utilize a fórmula abaixo:

                                                IMC = peso / altura2
"""
peso = float(input("Digite o seu peso: "))
alt = float(input("Digite a sua altura: "))

IMC = peso/(alt**2)

print(f"O seu IMC é {IMC}")
