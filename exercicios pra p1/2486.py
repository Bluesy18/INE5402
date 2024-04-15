def verifica0 (t):
  while((t < 1) or (t > 7)):
    t = int(input("Quantidade inválida! Digite novamente quantos alimentos diferentes você come diariamente: "))

def interpreta (n, a):
  c = 0
  if (a == "suco de laranja"):
    c += n*120

  elif (a == "morango fresco"):
    c += n*85

  elif(a == "mamao"):
    c += n*85

  elif(a == "goiaba vermelha"):
    c += n*70

  elif(a == "manga"):
    c += n*56

  elif(a == "laranja"):
    c += n*50

  elif(a == "brocolis"):
    c += n*34
    

  return c

def diferenca (c):
  if(110 <= c <= 130):
    return f"{c} mg"

  elif (c > 130):
    return f"Menos {c-130} mg"
  
  elif (c < 110):
    return f"Mais {110-c} mg"

c = 0  
t = int(input("Digite quantos alimentos diferentes você come diariamente: "))

while (t != 0):
  for i in range (t):
    n, a = input("Digite quantos e quais alimentos você come (separados por espaço): ").split(" ", 1)
    n = int(n)
    c += interpreta(n, a)

  print(diferenca(c))
  c = 0
  t = int(input("Digite quantos alimentos diferentes você come diariamente: "))
