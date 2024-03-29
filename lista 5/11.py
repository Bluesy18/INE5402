### 11 ###

# Cria variável z
z = -1

# Cria variável de contagem
cont = 1

# Cria variável de soma
soma = 0

# Usuário digita valores de x e de z
x = int(input("Digite um número inteiro: "))
z = int(input("Digite outro número inteiro: "))

# Se valor for negativo, fecha o programa
if (x < 0):
  print("Tente novamente")

else:

  # Enquanto valor de z for menor ou igual a x, pede outro valor para z
  while (z <= x):
    z = int(input("Digite outro número inteiro: "))
  
  # Enquanto a soma dos valores for menor ou igual a z, acrescenta o próximo número da sequência
  while (soma <= z):
   cont += 1
   x += 1
   soma += x
  
  # Mostra quantos números foram necessários somar
  print(cont)