### 2339 ###

# Usuário digita a quantidade de competidores, folhas de papel compradas e folhas de papel para cada competidor
c, p, f = map(int, input("Digite a quantidade de competidores, de folhas compradas e a quantidade de folhas por competidor (separado por espaço): ").split())

# Conversão para inteiro
c1 = int(c)
p1 = int(p)
f1 = int(f)

if(c1 < 1 or c1 > 1000):
  print("Quantidade inválida")

elif(p1 < 1 or p1 > 1000):
  print("Quantidade inválida")

elif(f1 < 1 or f1 > 1000):
  print("Quantidade inválida")

else:
  if((p1/c1) >= f1):
    print("S")

  else:
    print("N")