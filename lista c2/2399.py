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
