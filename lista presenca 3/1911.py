### 1911 ###

n = int(input("Digite a quantidade de assinaturas existentes: "))

while (n > 0):
  assinaturas = {}
  fake = 0
  for i in range(n):
    nome, assinaturas[nome] = input("Digite o nome do aluno e sua assinatura original: ").split()

  m = int(input("Digite quantas assinaturas deseja conferir: "))
  for j in range(m):
    nome2, assinatura2 = input("Digite o nome do aluno e a assinatura na sala: ").split()
    if (assinaturas.get(nome2) != assinatura2):
      fake += 1

  print(fake)
  n = int(input("Digite a quantidade de assinaturas existentes: "))


  
