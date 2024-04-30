### 1547 ###
def verifica0(qt, s):
  while ((qt < 4) or (qt > 10) or (s < 1) or (s > 100)):
    qt, s = map(int, input("Valores incorretos! Digite novamente a quantidade de alunos no grupo e qual o número a ser descoberto: ").split())

  return qt, s


def verifica1(grupo, qt):
  while (len(grupo) != qt):
    grupo = [int(x) for x in (input(f"Quantidade incorreta de alunos! Digite os valores de {qt} alunos: ")).split()]

  return grupo

melhorAluno = ""
melhorDiferenca = 0

n = int(input("Digite quantas camisetas serão sorteadas: "))

for i in range(n):
  qt, s = map(int, input("Digite a quantidade de alunos no grupo e qual o número a ser descoberto: ").split())
  qt, s = verifica0(qt, s)

  grupo = [int(x) for x in (input(f"Digite os valores de {qt} alunos: ")).split()]
  grupo = verifica1(grupo, qt)

  for j in range (qt):
    dif = s - grupo[j]

    if (dif < 0):
      dif = dif*-1

    if (j == 0):
      melhorAluno = j+1
      melhorDiferenca = dif

    if (j != 0):
      if(dif < melhorDiferenca):
        melhorDiferenca = dif
        melhorAluno = j+1

  print(f"O valor mais próximo do número foi do aluno {melhorAluno}")



