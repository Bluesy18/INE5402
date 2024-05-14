### 7 ###

def calcMedia(info):
  soma = 0
  for p in info:
    soma += p

  media = round((soma/3), 2)

  return soma, media

def verifica0 (info):
  for n in info:
      if((n < 0) or (n > 10)):
        certo = 0
        break
      else:
        certo = 1
  while (certo == 0):
    info = [float(x) for x in (input(f"Notas inválidas! Digite novamente as 3 notas do aluno {nome}: ")).split()]
    for n in info:
      if((n < 0) or (n > 10)):
        certo = 0
        break
      else:
        certo = 1

  return info

def verifica1(consulta):
  for l in boletim:
      if(consulta == l[1]):
        igual = 1
        break
      else:
        igual = 0
  while (igual == 0):
    consulta = input("Nome inválido! Digite novamente o nome do aluno que desejas consultar: ")
    for l in boletim:
      if(consulta == l[1]):
        igual = 1
        break

  return consulta

alunos = []
info = []
boletim = []

n = int(input("Digite quantos alunos deseja informar: "))

for i in range (n):
  nome = input(f"Digite o nome do {i+1}º aluno: ")
  info = [float(x) for x in (input(f"Digite as 3 notas do aluno {nome}: ")).split()]
  soma, media = calcMedia(info)
  info = verifica0(info)
  info.append(media)
  info.append(nome)
  alunos.append(info)
  boletim.append([media, nome])
  info = []

print(boletim)

res = input("Deseja consultar as notas individuais? (S/N): ").upper()

while (res == "S"):
  consulta = input("Digite o nome do aluno que desejas consultar: ")
  consulta = verifica1(consulta)
  for m in alunos:
    if(consulta in m):
      print(f"Notas individuais: {m[0]}, {m[1]} e {m[2]}")

  res = input("Deseja consultar as notas individuais? (S/N): ").upper()
  
      
 