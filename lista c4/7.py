### 7 ###

# Define função para calcular a média
def calcMedia(info):
  soma = 0
  for p in info:
    soma += p

  media = round((soma/3), 2)

  return soma, media

# Define funções para verificar listas "info" e "consulta"
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

# Cria listas de alunos, infos e boletim
alunos = []
info = []
boletim = []

# Usuário digita quantos alunos irá informar
n = int(input("Digite quantos alunos deseja informar: "))

# Usuário digita nome do aluno e suas 3 notas e a partir disso, separa informações em seus devidos lugares
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

# Mostra boletim
print(boletim)

# Usuário digita se deseja consultar notas individuais
res = input("Deseja consultar as notas individuais? (S/N): ").upper()

# Se sim...
while (res == "S"):

  # Usuário digita nome do aluno que deseja consultar
  consulta = input("Digite o nome do aluno que desejas consultar: ")
  consulta = verifica1(consulta)
  
  # Consulta e mostra notas individuais
  for m in alunos:
    if(consulta in m):
      print(f"Notas individuais: {m[0]}, {m[1]} e {m[2]}")

  # Continua loop
  res = input("Deseja consultar as notas individuais? (S/N): ").upper()
  
      
 