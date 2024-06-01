### 1261 ###

cargos = []
salarios = {}

n, m = map(int, input("Digite quantos cargos existem e quantas descrições haverão (separado por espaço): ").split())

for i in range (n):
  cargo, salarios[cargo] = input("Digite o nome do cargo e o respectivo salário (separado por espaço): ").split()
  salarios[cargo] = int(salarios[cargo])
  cargos.append(cargo)

for j in range(m):
  desc = ""
  salarioTotal = 0
  while True:
    desc = input("Digite a descrição: ")
    if (desc == "."):
      break
    else:
      for l in cargos:
        if (l in desc):
          cont = desc.count(l)
          salarioTotal += (salarios.get(l)*cont)
  print(salarioTotal)

