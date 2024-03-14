### 1008 ###

# Usuário digita suas informações
numero = int(input("Digite seu número: "))
horas = float(input("Digite suas horas trabalhadas: "))
phora = float(input("Digite o quanto você recebe por hora: "))

# Cálculo e arredondamento do salário
salario = horas*phora
salarioA = round(salario, 2)

# Número e salário
print(f"NUMBER = {numero}\nSALARY = U$ {salarioA}")