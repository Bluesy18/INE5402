### 1471 ###

def verifica0(n, r):
  while (((r > n) and (r!= 0) and (n != 0)) or (n < 1 and (n != 0)) or (r < 1 and r!= 0)):
    n, r = map(int, input("Valores inválidos! Digite novamente quantos mergulhadores mergulharam e quantos voltaram: ").split())

  return n, r

def verifica1(volt):
  while (len(volt) != r):
    volt = [int(x) for x in (input(f"Valores inválidos! Digite novamente a identificação dos {r} mergulhadores que voltaram (separados por espaço): ")).split()]

  return volt

def resultado(merg):
  if (len(merg) == 0):
    res = "*"

  else:
    res = merg

  return res

n, r = map(int, input("Digite quantos mergulhador(es) mergulharam e quantos voltaram: ").split())
n, r = verifica0(n, r)

while ((n != 0) and (r != 0)):

  merg = list(range(1, n+1))

  volt = [int(x) for x in (input(f"Digite a identificação dos {r} mergulhadores que voltaram (separados por espaço): ")).split()]
  volt = verifica1(volt)

  for i in range (len(volt)):
    merg.remove(volt[i])

  res = resultado(merg)
  print(*res)

  n, r = map(int, input("Digite quantos mergulhadores mergulharam e quantos voltaram: ").split())
  n, r = verifica0(n, r)
