### 1048 ###

# Usuário digita seu salário
sal = round(float(input("Digite seu salário: ")), 2)

# Verifica o valor do salário e aplica o reajuste
if(0 <= sal <= 400.00):
  rea = round((sal*0.15), 2)
  nsal = round((sal + rea), 2)
  perc = 15

elif(400.01 <= sal <= 800.00):
  rea = round((sal*0.12), 2)
  nsal = round((sal + rea), 2)
  perc = 12

elif(800.01 <= sal <= 1200.00):
  rea = round((sal*0.10), 2)
  nsal = round((sal + rea), 2)
  perc = 10

elif(1200.01 <= sal <= 2000.00):
  rea = round((sal*0.07), 2)
  nsal = round((sal + rea), 2)
  perc = 7

elif(sal > 2000.00):
  rea = round((sal*0.4), 2)
  nsal = round((sal + rea), 2)
  perc = 4

# Mostra os novos valores
print(f"Novo salário: {nsal}\nReajuste ganho: {rea}\nEm percentual: {perc}%")


