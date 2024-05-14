### 2 (1164) ###

def verifica0 (x):
  while ((x < 1) or (x > 20)):
    x = int(input("Número inválido! Digite novamente um número inteiro entre 1 e 20"))

  return x

n = int(input("Digite quantos casos você deseja testar: "))

divisores = []

for i in range (n):
  x = int(input("Digite um número inteiro entre 1 e 20: "))
  for j in range(x):
    if(j != 0):
      if(x % j == 0):
        divisores.append(j)
  soma = 0
  for p in divisores:
    soma += p
  if (soma == x):
    print(f"{x} eh perfeito")
  
  else:
    print(f"{x} não eh perfeito")
  divisores = []



