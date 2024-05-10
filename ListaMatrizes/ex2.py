"""
    Preencha uma matriz 10x10 com números aleatórios e exiba a matriz. A seguir, exiba o somatório
    dos elementos da diagonal secundária da matriz.
"""
import random

matrix = []
soma = 0


for i in range(10):
    linhas = []
    for j in range(10):
        random_num = random.randint(1,20)
        if i == j:
            linhas.append(random_num)
            soma += random_num
        else:
            linhas.append(random_num)
    matrix.append(linhas)

for i in range(10):
    for j in range(10):
        print(f"{matrix[i][j]}", end="\t")
    print()

print(f"A soma da diagonal é {soma}")