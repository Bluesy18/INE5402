''' 3 '''

def salario(sal, acre, per):
    sala = acre*sal
    dif = sala - sal
        
    print(f"""Novo salario: {sala}
Reajuste ganho: {dif}
Em percentual : {per}""")
    
sal = -1
    
while (sal < 0):
    sal = float(input("Digite seu salário: "))

if (sal <= 400.00):
        acre = 1.15
        per = "15%" #variante para determinar o percentual
    
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
        
if (sal >= 0):
    salario(sal, acre, per)
