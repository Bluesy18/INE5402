### 1953 ###

dicio  = {"EPR" : 0, "EHD": 0, "INTRUSOS": 0}

n = int(input("Digite quantos alunos estão na sala: "))

while (n != 0):

  for i in range(n):
    matri, sigla = input("Digite sua matricula e a sigla do seu curso: ").split()
    if (sigla == "EPR"):
      dicio["EPR"] += 1
    elif (sigla == "EHD"):
      dicio["EHD"] += 1
    else:
      dicio["INTRUSOS"] += 1

  print(f"EPR: {dicio['EPR']}\nEHD: {dicio['EHD']}\nINTRUSOS: {dicio['INTRUSOS']}")
  n = int(input("Digite quantos alunos estão na sala: "))

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

### 2478 ###

amigoSec = {}
resp = "S"

n = int(input("Digite a quantidade de participantes do amigo secreto: "))

for i in range (n):
  digitado = input("Digite o nome da pessoa e seus presentes desejados: ")
  listaDig = digitado.split(" ", 1)
  nomeDig = listaDig[0]
  amigoSec[nomeDig] = listaDig[1]

while (resp == "S"):
  acertou = 0

  escolha = input("Digite o nome do amigo secreto e os presentes que ele irá receber: ")
  listaEsc = escolha.split(" ", 1)
  nomeEsc = listaEsc[0]
  presentesEsc = listaEsc[1].split(" ")

  for l in presentesEsc:
    if (l in amigoSec.get(nomeEsc, "Tente Novamente!")):
      acertou = 1

  if(acertou == 0):
    print("Tente Novamente!")
  
  else:
    print("Uhul! Seu amigo secreto vai adorar o/")

  resp = input("Deseja tentar acertar as escolhas novamente? (S/N): ").upper()

### 1430 ###

notas = {"W":1, "H":0.5, "Q":0.25, "E":0.125, "S":0.0625, "T":0.03125, "X":0.015625}

composicoes = input("Digite suas composições (separadas por /): ").split("/")

while (composicoes != ["*"]):
  compasso = 0
  corretas = 0
  del composicoes[0]
  del composicoes[-1]
  for l in composicoes:
    for m in l:
      compasso += notas.get(m)
    if (compasso == 1):
      corretas += 1
    compasso = 0
  
  print(corretas)
  
  composicoes = input("Digite suas composições (separadas por /): ").split("/")
