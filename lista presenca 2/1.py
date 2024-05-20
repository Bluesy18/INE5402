### 1 ###

def verifica0 (modalidade, modalidadesStr):
  while (modalidade not in modalidadesStr):
    modalidade = input("Modalidade inválida! Digite novamente a modalidade na qual o aluno será matriculado: ").lower()
  return modalidade

futebol = {"Lucas"}
natacao = {"Davi"}
volei = {"Henrique"}
basquete = {"Arthur"}

modalidadesStr = ["futebol", "natação", "vôlei", "basquete"]
modalidades = [futebol, natacao, volei, basquete]

desconto = []
print(f"Alunos matriculados em:\nFutebol: {", ".join(str(_) for _ in futebol)}\nNatação: {", ".join(str(_) for _ in natacao)}\nVôlei: {", ".join(str(_) for _ in volei)}\nBasquete: {", ".join(str(_) for _ in basquete)}\n")

resp1 = input("Deseja matricular um novo aluno em alguma modalidade? (S/N): ").upper()
while (resp1 == "S"):
  aluno = input("Digite o nome do novo aluno: ")
  resp2 = "S"
  while (resp2 == "S"):
    modalidade = input("Digite a modalidade na qual o aluno será matriculado: ").lower()
    modalidade = verifica0(modalidade, modalidadesStr)
    modalidades[modalidadesStr.index(modalidade)].add(aluno)
    resp2 = input("Deseja matricular o aluno em mais alguma modalidade? (S/N): ").upper()
  resp1 = input("Deseja matricular um novo aluno em alguma modalidade? (S/N): ").upper()

for i in range (3):
  for j in range(3, i, -1):
    intersec = modalidades[i].intersection(modalidades[j])
    if((intersec != set()) and (intersec not in desconto)):
        desconto.append(intersec)

desconto2 = []

for q in desconto:
  desconto2.append(*q)

print(f"Alunos matriculados em:\nFutebol: {", ".join(str(_) for _ in futebol)}\nNatação: {", ".join(str(_) for _ in natacao)}\nVôlei: {", ".join(str(_) for _ in volei)}\nBasquete: {", ".join(str(_) for _ in basquete)}\n")

if (len(desconto2) != 0):
  print(f"O(s) aluno(s) com desconto é/são: {", ".join(str(_) for _ in desconto2)}\n")

else:
  print("Não existem alunos com desconto.")

print(f"O número de alunos matriculados em cada modalidade é:\nFutebol: {len(futebol)}\nNatação {len(natacao)}\nVôlei: {len(volei)}\nBasquete: {len(basquete)}\nTotal: {len(futebol.union(natacao, volei, basquete))}\n")





  
