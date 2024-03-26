### 7 ###

# Cria as variáveis de contagem
contA = 0
contG = 0
contD = 0

# Usuário digita qual combustível ele deseja
comb = int(input("Digite o número do combústivel -> 1.Álcool 2.Gasolina 3.Diesel 4.Fim: "))
    
# Enquanto o número digita obedecer o intervalo, contabiliza o número digitado para a contagem correspondente, pergunta novamente o número do combustível e finaliza o processo quando o número 4 é digitado
while (1 <= comb <= 4):
    if(comb == 1):
            contA += 1
    
    elif(comb == 2):
            contG += 1
            
    elif(comb == 3):
            contD += 1
            
    elif(comb == 4):
        break
    comb = int(input("Digite o número do combústivel -> 1.Álcool 2.Gasolina 3.Diesel 4.Fim: "))        
    
# Mostra a quantidade pedida de cada combustível
print(f"MUITO OBRIGADO\nAlcool: {contA}\nGasolina: {contG}\nDiesel: {contD}")
    