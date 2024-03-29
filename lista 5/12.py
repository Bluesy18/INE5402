### 12 ###

# Usuário digita coordenada da bola
x, y = map(int, input("Digite as coordenadas da bola (separados por espaço): ").split())

# Verifica e informa se bola está dentro ou fora
if((0 <= x <= 432) and (0 <= y <= 468)):
  print("dentro")

else:
  print("fora")