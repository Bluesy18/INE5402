### 1008 ###

numero = int(input("Digite seu número: "))
horas = float(input("Digite suas horas trabalhadas: "))
phora = float(input("Digite o quanto você recebe por hora: "))

salario = horas*phora
salarioA = round(salario, 2)

print(f"NUMBER = {numero}\n SALARY = U$ {salarioA}")