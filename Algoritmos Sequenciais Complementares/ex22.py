
alt = float(input("Digite a altura da cozinha: "))
lag = float(input("Digite a largura da cozinha: "))
comp = float(input("Digite a comprimento da cozinha: "))

total = 2*(alt*lag)+2*(comp*alt)

if total%1.5 == 0:
    caixa = total/1.5
else:
    caixa = total//1.5 +1

print(f'Serão necessárias {caixa} caixas de azulejos')
