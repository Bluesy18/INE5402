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
