### 3 ###

# Função calcula novo salário e diferença do atual com o anterior e mostra pro usuário além desses valores, o acréscimo em percentual
def salario(sal, acre, per):
    sala = acre*sal
    dif = sala - sal
        
    print(f"Novo salario: {sala}\nReajuste ganho: {dif}\nEm percentual : {per}")
    
sal = -1

# Enquanto salário for negativo, continua pedindo para usuário digitar o salário
while (sal < 0):
    sal = float(input("Digite seu salário: "))

# Interpreta qual será o valor do acréscimo, baseado no salário digitado
if (sal <= 400.00):
        acre = 1.15
        per = "15%"
    
elif (sal <= 800.00):
        acre = 1.12
        per = "12%"
        
elif (sal <= 1200.00):
        acre = 1.10
        per = "10%"
        
elif (sal <= 2000.00):
        acre = 1.07
        per = "7%"
        
elif (sal > 2000.00):
        acre = 1.04
        per = "4%"

# Chama função para calcular salário        
if (sal >= 0):
    salario(sal, acre, per)
