
brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos validos: "))

total = brancos + nulos + validos

per_b = (brancos/total)*100
per_n = (nulos/total)*100
per_val = (validos/total)*100

print(f'O percentual para votos brancos, nulos e válidos foram, respectivamente, {per_b}%,{per_n}% e {per_val}%')
