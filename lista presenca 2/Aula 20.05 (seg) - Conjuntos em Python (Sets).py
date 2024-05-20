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

## 1 ##
print(f"Alunos matriculados em:\nFutebol: {", ".join(str(_) for _ in futebol)}\nNatação: {", ".join(str(_) for _ in natacao)}\nVôlei: {", ".join(str(_) for _ in volei)}\nBasquete: {", ".join(str(_) for _ in basquete)}\n")

## 2 ##
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

## 3 ##
for i in range (3):
  for j in range(3, i, -1):
    intersec = modalidades[i].intersection(modalidades[j])
    if((intersec != set()) and (intersec not in desconto)):
        desconto.append(intersec)

desconto2 = []

for q in desconto:
  desconto2.append(*q)

## 1 ##
print(f"Alunos matriculados em:\nFutebol: {", ".join(str(_) for _ in futebol)}\nNatação: {", ".join(str(_) for _ in natacao)}\nVôlei: {", ".join(str(_) for _ in volei)}\nBasquete: {", ".join(str(_) for _ in basquete)}\n")

## 3 ##
if (len(desconto2) != 0):
  print(f"O(s) aluno(s) com desconto é/são: {", ".join(str(_) for _ in desconto2)}\n")

else:
  print("Não existem alunos com desconto.\n")

## 4 ##
print(f"O número de alunos matriculados em cada modalidade é:\nFutebol: {len(futebol)}\nNatação {len(natacao)}\nVôlei: {len(volei)}\nBasquete: {len(basquete)}\nTotal: {len(futebol.union(natacao, volei, basquete))}\n")

### 2 ###

def verifica0 (escolha):
  while ((escolha != 1) and (escolha != 2)):
    escolha = int(input("Empresa inválida! Digite novamente em qual empresesa deseja cadastrar o cliente: "))
  return escolha

empresa1 = {"André", "Davi"}
empresa2 = {"Thiago", "Pedro"}

## 1 ##
print(f"\nClientes:\nEmpresa 1: {", ".join(str(_) for _ in empresa1)}\nEmpresa 2: {", ".join(str(_) for _ in empresa2)}\n")

## 2 ##
resp1 = input("Deseja cadastrar novo cliente? (S/N): ").upper()
while (resp1 == "S"):
  cliente = input("Digite o nome do novo cliente: ")
  resp2 = "S"
  while (resp2 == "S"):
    escolha = int(input("Digite em qual empresesa deseja cadastrar o cliente: "))
    escolha = verifica0(escolha)
    if (escolha == 1):
      empresa1.add(cliente)
    else:
      empresa2.add(cliente)
    resp2 = input("Deseja cadastrar cliente em mais uma emprese? (S/N): ").upper()
  resp1 = input("Deseja cadastrar novo cliente (S/N): ").upper()

  nasDuas = [empresa1.intersection(empresa2)]
  nasDuas2 = []

  for q in nasDuas:
    nasDuas2.append(*q)

## 1 ##
print(f"\nClientes:\nEmpresa 1: {", ".join(str(_) for _ in empresa1)}\nEmpresa 2: {", ".join(str(_) for _ in empresa2)}\n")

## 3 ##
if (len(nasDuas2) != 0):
  print(f"O(s) cliente(s) cadastrado(s) nas duas empresas é/são: {", ".join(str(_) for _ in nasDuas2)}\n")

else:
  print("Não existem clientes cadastrados nas duas empresas\n")

## 4 ##
print(f"Quantidade de clientes na:\nEmpresa 1: {len(empresa1)}\nEmpresa 2: {len(empresa2)}\nEm ambas: {len(nasDuas2)}\nEm apenas uma: {len(empresa1.symmetric_difference(empresa2))}\nTotal: {len(empresa1.union(empresa2))}\n")
    




  
