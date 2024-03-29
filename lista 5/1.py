### 1 ###

# Cria variável de resposta
r = "S"

# Cria variáveis dos jogadores
j1 = "pedra"
j2 = "papel"

while r=="S":
    # Jogadores decidem jogada
    j1 = input("Digite pedra, papel ou tesoura: ").lower()
    j2 = input("Digite pedra, papel ou tesoura: ").lower()
    
    # Verifica escolhas e mostra resultado
    if(j1 == j2):
        r = input("Empatou. Deseja continuar jogando? (S/N): ").upper()
        
    elif((j1 != "pedra") and (j1 != "papel") and (j1 != "tesoura")) or ((j2 != "pedra") and (j2 != "papel") and (j2 != "tesoura")):
        r = input("Opção inválida. Deseja tentar novamente? (S/N): ").upper()
        
    elif ((j1 == "pedra" and j2 == "papel") or (j1 == "papel" and j2 == "tesoura") or (j1 == "tesoura" and j2 == "pedra")):
        r = input("J2 ganhou. Deseja continuar jogando? (S/N): ").upper()
        
    elif ((j2 == "pedra" and j1 == "papel") or (j2 == "papel" and j1 == "tesoura") or (j2 == "tesoura" and j1 == "pedra")):
        r = input("J1 ganhou. Deseja continuar jogando? (S/N): ").upper()
        
    
    



