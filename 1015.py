### 1015 ###

# Usuário digita as coordenadas dos pontos

x1 = float(input("Digite x1: "))
x2 = float(input("Digite x2: "))
y1 = float(input("Digite y1: "))
y2 = float(input("Digite y2: "))

# Cálculo da distância entre dois pontos
dab = ((x2-x1)**2 + (y2-y1)**2)**1.0/2

# Apresenta a distância entre os dois pontos ao usuário
print(f"A distãncia entre os pontos é {dab}")