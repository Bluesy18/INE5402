### 6 ###

saltos = []
nome = input("Digite o nome do atleta: ")

while nome != "o" and nome != "O" :
    
    for i in range (5):
        saltos.append(float(input(f"Digite a distância do {i+1}º salto: ")))
        
    saltoOrdem = saltos[:] 
    
    for i in range (4):
        if saltos[0] > saltos[1]:
            saltos[0], saltos[1] = saltos[1], saltos[0]
        if saltos[1] > saltos[2]:
            saltos[1], saltos[2] = saltos[2], saltos[1]
        if saltos[2] > saltos[3]:
            saltos[2], saltos[3] = saltos[3], saltos[2]
        if saltos[3] > saltos[4]:
            saltos[3], saltos[4] = saltos[4], saltos[3]
            
    media = round(((saltos[1]+saltos[2]+saltos[3])/3), 1) 
    
    print(f"""Atleta: {nome}

Primeiro Salto: {saltoOrdem[0]} m
Segundo Salto: {saltoOrdem[1]} m
Terceiro Salto: {saltoOrdem[2]} m
Quarto Salto: {saltoOrdem[3]} m
Quinto Salto: {saltoOrdem[4]} m

Melhor salto:  {saltos[4]} m
Pior salto: {saltos[0]} m
Média dos demais saltos: {media} m

Resultado final:
{nome}: {media} m""")
    nome = input("Digite o nome do atleta: ")
    
        


        
        
        