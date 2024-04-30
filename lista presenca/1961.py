### 1961 ###

def verifica0(p, n):
  while ((p < 1) or (p > 5) or (n < 2) or (n > 100)):
    p, n = map(int, input("Valores inválidos! Digite a altura do pulo do sapo e a quantidade de canos (separados por espaço): ").split())

  return p, n

def verifica1(hcanos):
  while (len(hcanos) != n):
    hcanos = [int(x) for x in (input(f"Valores inválidos! Digite a altura de  {n} cano(s) (separados por espaço): ")).split()]

  return hcanos

def res(gameover):
  if (gameover == 0):
    res = "YOU WIN"

  else:
    res = "GAME OVER"

  return res


gameover = 0

p, n = map(int, input("Digite a altura do pulo do sapo e a quantidade de canos (separados por espaço): ").split())
p, n = verifica0(p, n)

hcanos = [int(x) for x in (input(f"Digite a altura de  {n} cano(s) (separados por espaço): ")).split()]
hcanos = verifica1(hcanos)

for i in range (len(hcanos) - 1):
  dif = hcanos[i+1] - hcanos[i]

  if(dif < 0 ):
    dif = dif*-1

  if(dif > p):
    gameover = 1
    break

print(res(gameover))
