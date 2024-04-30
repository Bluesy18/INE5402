### 5 ###

def verifica0(n):
  while ((n < 2) or (n > 100)):
    n = int(input("Valores inválidos! Digite novamente um inteiro: "))

  return n

def verifica1(listaInc):
  while (len(listaInc) != (n-1)):
    listaInc = [int(x) for x in (input(f"Valores inválidos! Digite {n-1} números da sequência novamente: ")).split()]

  return listaInc

n = int(input("Digite um inteiro: "))
n = verifica0(n)

lista = list(range(1, n+1))

listaInc = [int(x) for x in (input(f"Digite {n-1} números da sequência: ")).split()]
listaInc = verifica1(listaInc)

for i in range (len(listaInc)):
  lista.remove(listaInc[i])

print(*lista)

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

### 1533 ###

def verifica0(n):
  while (((n < 2) and (n != 0)) or (n > 1000)):
    n = int(input("Valor inválido! Digite novamente a quantidade de suspeitos: "))

  return n

n = int(input("Digite a quantidade de suspeitos: "))
n = verifica0(n)

while (n != 0):
    sus = [int(x) for x in (input("Digite quais são os suspeitos (separados por espaço): ")).split()]
    
    susOrd = sorted(sus)
    
    culpado = susOrd[len(susOrd) - 2]
    
    for i in range(len(sus)):
    
        if culpado == sus[i]:
          culpadoIndice = i + 1
    
    print(f" O índice do culpado é {culpadoIndice}")
    
    n = int(input("Digite a quantidade de suspeitos: "))
    n = verifica0(n)

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

### 2060 ###

def verificaN(n):
  while((n < 1) or (n > 1000)):
    n = int(input("Valor inválido! Digite a quantidade de números na lista novamente: "))

  return n

n = int(input("Digite a quantidade de números na lista: "))
n = verificaN(n)

lista = [int(x) for x in (input(f"Digite {n} números inteiros (separados por espaço): ")).split()]
num = [2, 3, 4, 5]
cont = [0, 0, 0, 0]

for i in range (n):

  for j in range (len(cont)):
    if(lista[i] % num[j] == 0):
      cont[j] += 1

print(f"{cont[0]} Multiplo(s) de 2\n{cont[1]} Multiplo(s) de 3\n{cont[2]} Multiplo(s) de 4\n{cont[3]} Multiplo(s) de 5\n")

