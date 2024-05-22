### 1281 ###

def somador(preco, qntd, precoTotal):
  precoTotal += preco*qntd

  return precoTotal

def verifica0(nome, qntd, precoTotal):
  existe = 0
  while True:
    for l in produtos:
      if ((nome in l.values()) and (qntd >= 1)):
        existe = 1
        break
    if (existe == 1):
      preco = l.get("preço")
      precoTotal = somador(preco, qntd, precoTotal)
      break
    else:
      nome, qntd = input("Algo deu errado! Digite novamente o nome e quantidade comprada: ").split()
      qntd = int(qntd)
  
  return nome, qntd, precoTotal

def verifica1(p, m):
  while (p > m):
    p = int(input("Quantiade inválida! Digite novamente a quantidade de produtos diferentes que serão comprados: "))

  return p

n = int(input("Digite a quantidade de idas à feira: "))

for i in range(n):
  precoTotal = 0
  produtos = []
  m = int(input("Digite a quantidade de produtos que estão disponíveis para compra: "))
  for j in range(m):
    prod = {}
    prod["nome"], prod["preço"] = input("Digite o nome e o preço do produto: ").split()
    prod["preço"] = float(prod["preço"])
    produtos.append(prod)
  p = int(input("Digite a quantidade de produtos diferentes que serão comprados: "))
  p = verifica1(p, m)
  for k in range(p):
    nome, qntd, = input("Digite o nome e quantidade comprada: ").split()
    qntd = int(qntd)
    nome, qntd, precoTotal = verifica0(nome, qntd, precoTotal)
  print(f"R$ {round(precoTotal, 2)}")
