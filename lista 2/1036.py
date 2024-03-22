### 1036 ###

# Usuário digita os valores
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula discriminante
delta = (b**2) - 4 * a * c

# Calcula (ou não) raízes
if (delta < 0 or a == 0):
  print ("Impossível calcular")
else:
  r1 = (-b + (delta**0.5))/(2*a)
  r2 = (-b - (delta**0.5))/(2*a)

  r1r = round(r1, 5)
  r2r = round(r2, 5)

# Apresenta raízes ao usuário
  print(f"R1 = {r1r}\nR2 = {r2r}")