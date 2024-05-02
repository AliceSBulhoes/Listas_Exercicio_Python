
seg = int(input("Digite um número inteiro em segundos: "))

hora = seg//3600
min = (seg//60) - 60
segun = seg%60

print(f'Esse npumero corresponde a {hora}h, {min} minutos e {segun}segundos')
