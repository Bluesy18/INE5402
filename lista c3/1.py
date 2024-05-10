### 1 ###

res = "S"
pessoas = []
info = []
pesados = []
leves = []
velhos = []


while res == "S":
    n = int(input("Quantas pessoas serão cadastradas: "))
    
    for i in range (n):
        info = input("Digite o nome, idade e peso (separado por espaço): ").split()
        if(i == 0):
            menorPeso = info[2]
            maiorPeso = info[2]
        else:
            if(info[2] >= maiorPeso):
                maiorPeso = info[2]
        
            if(info[2] <= menorPeso):
                menorPeso = info[2]
                
        pessoas.append(info[:])
    
    
    
    for p in pessoas:
        int(p[1])
        int(p[2])
        
        if (p[2] == maiorPeso):
            pesados.append(p[0])
            
        if (p[2] == menorPeso):
            leves.append(p[0])
            
        if (p[1] > "20"):
            velhos.append(p[1])
            
    print(f"{n} pessoas foram cadastradas.\nO(s) dono(s) do maior peso é/são: {pesados}\nO(s) dono(s) do menor peso é/são: {leves}\nAs pessoas acima de vinte anos são: {velhos}")
    
    res = input("Deseja continuar?(s ou n): ").upper()
    
        
    
        
        
         