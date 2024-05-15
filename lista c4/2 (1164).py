### 2 (1164) ###

# Verifica valor de x de acordo com as limitações
def verifica0 (x):
  while ((x < 1) or (x > 20)):
    x = int(input("Número inválido! Digite novamente um número inteiro entre 1 e 20"))

  return x

# Usuário digita quantos casos deseja testar
n = int(input("Digite quantos casos você deseja testar: "))

# Cria lista de divisores
divisores = []

# Usuário digita números inteiros de 1 a 20
for i in range (n):
  x = int(input("Digite um número inteiro entre 1 e 20: "))
  x = verifica0(x)
  # Se for divisor, adiciona à lista de divisores
  for j in range(x):
    if(j != 0):
      if(x % j == 0):
        divisores.append(j)
  soma = 0
  for p in divisores:
    soma += p

  # Se soma dos divisores for igual a x, x é perfeito, caso contrário, não é
  if (soma == x):
    print(f"{x} eh perfeito")
  
  else:
    print(f"{x} não eh perfeito")

  # Limpa lista de divisores
  divisores = []



