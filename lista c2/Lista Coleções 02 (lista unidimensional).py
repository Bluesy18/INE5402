### 1 ###

def verifica0(lista):
  while (len(lista) != 5):
    lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]

  return lista

def nove(lista):
  cont = lista.count(9)
  return cont

def tres(lista):
  if 3 in lista:
    pos = lista.index(3)
    return pos
  
  else:
    return "NaN"

def par(lista):
  parc = 0
  for i in range(len(lista)):
    if (lista[i] % 2 == 0):
      parc += 1
  return parc

lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]
lista = verifica0(lista)
cont = nove(lista)
pos = tres(lista)
parc = par(lista)

print(f"O número 9 apareceu {cont} vez(es), o primeiro 3 foi digitado na posição {pos} e existe(m) {parc} par(es)")

### 2 ###

import random

lista = []
for i in range (5):
  lista.append(random.randint(1, 50))

for i in range (4):
        if lista[0] > lista[1]:
            lista[0], lista[1] = lista[1], lista[0]
        if lista[1] > lista[2]:
            lista[1], lista[2] = lista[2], lista[1]
        if lista[2] > lista[3]:
            lista[2], lista[3] = lista[3], lista[2]
        if lista[3] > lista[4]:
            lista[3], lista[4] = lista[4], lista[3]

print(f"Lista: {lista}\nO maior número é o {lista[4]} e o menor é o {lista[0]}")

### 3 ###

def verifica0(lista, n):
  while (len(lista) != n):
    lista = [int(x) for x in (input("Digite 5 valores inteiros: ")).split()]

  return lista

n = int(input("Digite o tamanho de sua lista: "))

lista = [int(x) for x in (input(f"Digite {n} valores inteiros: ")).split()]
lista = verifica0(lista, n)

repetidos = []

for i in range (len(lista)):
  cont = lista.count(lista[i])
  if (cont > 1):
    if lista[i] not in repetidos:
      repetidos.append(lista[i])

if (len(repetidos) == 0):
  print("Não exitem números repetidos.")

else:
  print(*repetidos)

### 1172 ###

for i in range (10):
  x = int(input("Digite um valor do vetor: "))

  if (x <= 0):
    x = 1

  print(f"X[{i}] = {x}")

### 1173 ###

x = int(input("Digite um valor para N[0]: "))

for i in range (10):

  if (i == 0):
    print (f"N[{i}] = {x}")
    xPassado = x

  else:
    print(f"N[{i}] = {xPassado*2}")
    xPassado = xPassado*2
         
### 1547 ###
def verifica0(qt, s):
  while ((qt < 4) or (qt > 10) or (s < 1) or (s > 100)):
    qt, s = map(int, input("Valores incorretos! Digite novamente a quantidade de alunos no grupo e qual o número a ser descoberto: ").split())

  return qt, s


def verifica1(grupo, qt):
  while (len(grupo) != qt):
    grupo = [int(x) for x in (input(f"Quantidade incorreta de alunos! Digite os valores de {qt} alunos: ")).split()]

  return grupo

melhorAluno = ""
melhorDiferenca = 0

n = int(input("Digite quantas camisetas serão sorteadas: "))

for i in range(n):
  qt, s = map(int, input("Digite a quantidade de alunos no grupo e qual o número a ser descoberto: ").split())
  qt, s = verifica0(qt, s)

  grupo = [int(x) for x in (input(f"Digite os valores de {qt} alunos: ")).split()]
  grupo = verifica1(grupo, qt)

  for j in range (qt):
    dif = s - grupo[j]

    if (dif < 0):
      dif = dif*-1

    if (j == 0):
      melhorAluno = j+1
      melhorDiferenca = dif

    if (j != 0):
      if(dif < melhorDiferenca):
        melhorDiferenca = dif
        melhorAluno = j+1

  print(f"O valor mais próximo do número foi do aluno {melhorAluno}")

### 1743 ###

def verifica0(conectores1):
  while (len(conectores1) != 5):
    conectores1 = [int(x) for x in (input(f"Quantidade errada! Digite novamente 5 números (0 ou 1): ")).split()]

  return conectores1

res = "Y"

conectores1 = [int(x) for x in (input(f"Digite 5 números (0 ou 1): ")).split()]
conectores1 = verifica0(conectores1)

conectores2 = [int(x) for x in (input(f"Digite 5 números (0 ou 1): ")).split()]
conectores2 = verifica0(conectores2)

for i in range (5):
  if((conectores1[i] - conectores2[i]) == 0):
    res = "N"
    break

print(res)

### 2399 ###

def verifica0(x):
  while ((x != 0) and (x != 1)):
    x = int(input(f"Valor inválido! Digite novamente se existe (1) ou não existe (0) mina na célula {i}: "))

  return x

n = int(input("Digite quantas células existem no campo minado: "))

campo = []
varredura = []

for i in range (n):
  x = int(input(f"Digite se existe (1) ou não existe (0) mina na célula {i}: "))
  x = verifica0(x)
  campo.append(x)

for j in range (n):
  
  if (j == 0):
    varredura.append((campo[j]+campo[j+1]))

  elif (j == n-1):
    varredura.append((campo[j]+campo[j-1]))

  else:
    varredura.append((campo[j-1]+campo[j]+campo[j+1]))

for k in range (len(varredura)):
  print(varredura[k])


