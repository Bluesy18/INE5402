### 2409 ###

# Usuário digita as dimensões do colchão e da porta
a, b, c = map(int, input("Digite as dimensões do colchão (separadas por espaço): ").split())
h, l = map(int, input("Digite as dimensões da porta (separadas por espaço): ").split())

# Verifica se as dimensões são válidas
if((a < 1 or a > 300) or (b < 1 or b > 300) or (c < 1 or c > 300) or (h < 1 or h > 250) or (l < 1 or l > 250)):
  print("Dimensões inválidas.")

# Verifica se o colchão passa pela porta
elif(a <= h and b <= l) or (a <= l and b <= h):
  print("S")

elif(a <= h and c <= l) or (a <= l and c <= h):
  print("S")

elif(b <= h and c <= l) or (b <= l and c <= h):
  print("S")

else:
  print("N")