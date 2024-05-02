# Ex 3
"""
    O sistema de avaliação de determinada disciplina, é composto por três notas. Escreva um
    programa que solicita as notas de um aluno, calcula e exibe a média aritmética deste aluno.

"""
mat = float(input("Digite a sua nota da prova 1: "))
mat2 = float(input("Digite a sua nota de prova 2: "))
mat3 = float(input("Digite a sua nota de prova 3: "))

media = (mat+mat2+mat3)/3

print(f"Sua média em matemática ficou {media}")
