# EX1
"""
    Faça um algoritmo que solicita ao usuário as notas de três provas. Calcule a média aritmética e
    informe se o aluno foi Aprovado ou Reprovado (o aluno é considerado aprovado com a média igual
    ou superior a 6).
"""
nota1 = float(input("Digite a sua nota da prova de matemática: "))
nota2 = float(input("Digite a sua nota da prova de física: "))
nota3 = float(input("Digite a sua nota da prova de química: "))

media = (nota1+nota2+nota3)/3

if media >= 6:
    print("Você foi aprovado em exatas!")
else:
    print("Você é um repetente em exatas :C")
