
p = int(input("Digite o número de pães: "))
b = int(input("Digite o número de broas: "))

pao = 0.38
broas = 4.5

val = (p*pao) + (broas*b)
polp = val*0.1

print(f'O valor arrecado no dia foi de R%{val} e guardará na poupança R${polp: .2f}')
