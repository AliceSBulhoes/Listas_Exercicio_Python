"""
    Preencha uma matriz 6x6 com números aleatórios e multiplique cada elemento da matriz pelo maior
    elemento de sua linha. Escrever a matriz original e a modificada. 
"""
import random

matrix = []
matrix_mod = []

for i in range(6):
    linhas = []
    for j in range(6):
        random_num = random.randint(1,20)
        linhas.append(random_num)
    matrix.append(linhas)

for i in range(6):
    for j in range(6):
        print(f"{matrix[i][j]}", end="\t")
    print()

print("\n")
for i in range(6):
    maximo = max(matrix[i])
    linhas = []
    for j in range(6):
        num_multi = maximo*matrix[i][j]
        linhas.append(num_multi)
    matrix_mod.append(linhas)

for i in range(6):
    for j in range(6):
        print(f"{matrix_mod[i][j]}", end="\t")
    print() 