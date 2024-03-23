### 2375 ###

# Usuário digita o diâmetro da bola de boliche e depois as dimensões da caixa
n = int(input("Digite o diâmetro da bola: "))
a, l, p = map(int, input("Digite as dimensões da caixa (separadas por espaço): ").split())

if((n < 1 or n > 10000) or (a < 1 or a > 10000) or (l < 1 or l > 10000) or (p < 1 or p > 10000)):
  print("Dimensões inválidas.")

elif(n <= min(a, l, p)):
  print("S")

else:
  print("N")