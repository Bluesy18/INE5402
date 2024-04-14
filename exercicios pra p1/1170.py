def comida (c, d):
  while (1 < c):
    c = c/2
    d += 1

  return d

n = int(input("Digite quantos casos deseja analisar: "))
d = 0

for i in range (n):
  c = float(input("Digite a quantidade de comida disponível para Blobs: "))
  print(f"{comida(c, d)} dias")
  d = 0



  