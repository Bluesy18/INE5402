def verifica0 (t):
  while ((t < 2) or (t> 50)):
    t = int(input("Digite a quantidade de expressões e jogadores: "))

t = int(input("Digite a quantidade de expressões e jogadores: "))
verifica0(t)

for i in range (1, t+1):
  op = input("Digite a operação desejada: ")
  x, y = op.split()
  y, z = y.split("=")

for i in range (1, t+1):
  a = 1 
## em progresso ##