"""
    Preencha uma matriz 6x6 com o elemento 1 em todas as posições em que o índice de linha tem valor
    igual ao índice da coluna. Preencha os demais elementos com zero e exiba a matriz.
"""

matrix = []

for i in range(6):
    linhas = []
    for j in range(6):
        if i == j:
            linhas.append(1)
        else:
            linhas.append(0)
    matrix.append(linhas)

for i in range(6):
    for j in range(6):
        print(f"{matrix[i][j]}", end="\t")
    print()