"""
    Preencha uma matriz 4x4 com números informados pelo usuário e exiba a matriz. Na sequência, gere
    a transposta da matriz e exiba-a (matriz transposta é a matriz que se obtém da troca de linhas por
    colunas da matriz).
"""

matrix = []
matrix_transposta = []

for i in range(4):
    linhas = []
    for j in range(4):
        num = int(input("Digite um número: "))
        linhas.append(num)
    matrix.append(linhas)

for i in range(4):
    for j in range(4):
        print(f"{matrix[i][j]}", end="\t")
    print()

print("\n")

for i in range(4):
    linhas = []
    for x in range(4):
        for j in range(4):
            num = matrix[i][j]
            

for i in range(4):
    for j in range(4):
        print(f"{matrix_transposta[i][j]}", end="\t")
    print()

