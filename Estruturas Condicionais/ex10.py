# EX 10
"""
    Faça um algoritmo que solicite o salário fixo e o valor das vendas efetuadas pelo vendedor de uma
    empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00
    mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.
"""
salario = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor das vendas efetuadas: "))

com = vendas*0.03

if vendas <= 1500:
    final = com + salario
else:
    final = (vendas-1500)*0.05 + salario + com

print(f'O seu salário final é R$ {final: .2f}')