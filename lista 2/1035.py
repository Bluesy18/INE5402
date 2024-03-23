### 1035 ###

# Usuário digita os valores
a, b, c, d = input("Digite os valores de A, B, C e D (separados por espaço): ").split()

# Conversão para inteiro
a1 = int(a)
b1 = int(b)
c1 = int(c)
d1 = int(d)

# Verifica a condição imposta pelo problema e mostra se ela foi satisfeita ou não
if(b1 > c1 and d1 > a1 and (c1+d1) > (a1+b1) and c1 > 0 and d1 > 0 and (a1 % 2 == 0)):
  print("Valores aceitos")

else:
  print("Valores nao aceitos")