# Ex 8

"""
    Uma concessionária de veículos paga aos seus vendedores um salário base de R$ 2.500,00. Além
    disso, uma comissão de R$ 200,00 por cada carro vendido e 2% do valor total das vendas.
    Escreva um programa que solicite o nome do vendedor, a quantidade de carros vendidos e o valor
    total de suas vendas. O programa deve calcular e exibir o salário final do vendedor.
        Exemplo:
        Nome do vendedor: Paulo
        Quantidade de carros vendidos: 5
        Valor total das vendas: 300000.0
        O vendedor Paulo receberá um salário de R$ 9500.0
"""
com = 2500
nome = input("Vendedor: ")
quant = int(input("Quantidade de carros vendidos: "))
total = float(input("Valor total das vendas: "))

sale = com + (quant*200) + (total*0.02)

print(f"O vendedor {nome} receberá um salário de R$ {sale}")
