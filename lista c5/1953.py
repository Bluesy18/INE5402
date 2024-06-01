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
