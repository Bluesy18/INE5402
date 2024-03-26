### 3 ###

# Cria variável de resposta e define ela como "S"
resp = "S"

# Cria a variável de porcentagem
porcentagem = 0

# Enquanto a resposta for "S", pede para o usuário digitar seu salário
while (resp == "S"):
    sal = float(input("Digite seu salário: "))

    # Calcula o desconto
    desc = sal*0.11

    # Se o desconto ultrapassar o valor de 320, o deconto passa a ser 320
    if (desc > 320.00):
        
        # Calcula porcentagem equivalente de 320 em relação ao salário
        porcentagem = sal/32000.00
        print(f"A porcentagem aplicada foi de {porcentagem}")

    # Verifica se a resposta continua "S" ou não
    resp = input("Deseja verificar novamente? (S/N): ").upper()
    
