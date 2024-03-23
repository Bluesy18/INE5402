### 1045 ###

# Usuário digita os valores dos lados do triângulo
c, b, a = input("Digite os valores de C, B e A (separados por esaço) respectivamente, sendo A o maior lado: ").split()

# Conversão para racional
a1 = float(a)
b1 = float(b)
c1 = float(c)

# Verifica se é um triângulo
if(a1 >= (b1+c1)):
  print("NAO FORMA TRIANGULO")

# Classifica o triângulo
else:
  if((a1**2) == ((b1**2)+(c1**2))):
    print("TRIANGULO RETANGULO")

  elif((a1**2) > ((b1**2)+(c1**2))):
    print("TRIANGULO OBTUSANGULO")

  elif((a1**2) < ((b1**2)+(c1**2))):
    print("TRIANGULO ACUTANGULO")

  if(a1 == b1 == c1 == a1):
    print("TRIANGULO EQUILATERO")

  elif((a1 == b1) ^ (b1 == c1) ^ (c1 == a1)):
    print("TRIANGULO ISOSCELES")



