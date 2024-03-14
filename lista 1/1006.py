### 1006 ###

# Usuário digita suas notas
A = float(input("Digite sua primeira nota (limite de uma casa decimal): "))
B = float(input("Digite sua segunda nota (limite de uma casa decimal): "))
C = float(input("Digite sua terceira nota (limite de uma casa decimal): "))

# Aplicação de pesos
Ap = A*2
Bp = B*3
Cp = C*5

# Cálculo e arredondamento da média
media = (Ap+Bp+Cp)/10
mediaA = round(media, 1)

# Média
print(f"MEDIA = {mediaA}")