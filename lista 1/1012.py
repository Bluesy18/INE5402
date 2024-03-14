### 1012 ###

# Definição de pi
pi = 3.14159

# Usuário digita seus valores
a = float(input("Digite o valor de A (uma casa decimal): "))
b = float(input("Digite o valor de B (uma casa decimal): "))
c = float(input("Digite o valor de C (uma casa decimal): "))

# Arredondamento dos valores
A = round(a, 1)
B = round(b, 1)
C = round(c, 1)

# a) Cálculo da altura do triângulo retângulo
areaTri = A*C/2

# b) Cálculo da área do circulo
areaCir = pi*C**2

# c) Cálculo da área do trapézio
areaTra = (A+B)*C/2

# d) Cálculo da área do quadrado
areaQua = B**2

# e) Cálculo da área do retângulo
areaRet = A*B

# Arredondamento das áreas
areaTriA = round(areaTri, 3)
areaCirA = round(areaCir, 3)
areaTraA = round(areaTra, 3)
areaQuaA = round(areaQua, 3)
areaRetA = round(areaRet, 3)

# Resposta mostrando as áreas
print(f"TRIANGULO: {areaTriA}\nCIRCULO: {areaCirA}\nTRAPEZIO: {areaTraA}\nQUADRADO: {areaQuaA}\nRETANGULO: {areaRetA}")