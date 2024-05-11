### 1 ###

# Cria listas vazias e variável de resposta
res = "S"
pessoas = []
info = []
pesados = []
leves = []
velhos = []

# Enquanto resposta for "S"
while res == "S":
    # Usuário digita quantas pessoas serão cadastradas
    n = int(input("Quantas pessoas serão cadastradas: "))
    
    for i in range (n):
        # Usuário digita as informações
        info = input("Digite o nome, idade e peso (separado por espaço): ").split()

        # Interpreta e define o maior e o menor peso
        if(i == 0):
            menorPeso = info[2]
            maiorPeso = info[2]
        else:
            if(info[2] >= maiorPeso):
                maiorPeso = info[2]
        
            if(info[2] <= menorPeso):
                menorPeso = info[2]
                
        pessoas.append(info[:])
    
    
    # Transforma em inteiros
    for p in pessoas:
        int(p[1])
        int(p[2])
        
        # Interpreta qual(quais) pessoa(s) tem o maior e o menor peso, além de quais têm mais de 20 anos
        if (p[2] == maiorPeso):
            pesados.append(p[0])
            
        if (p[2] == menorPeso):
            leves.append(p[0])
            
        if (p[1] > "20"):
            velhos.append(p[1])

    # Mostra resultado para o usuário
    print(f"{n} pessoas foram cadastradas.\nO(s) dono(s) do maior peso é/são: {pesados}\nO(s) dono(s) do menor peso é/são: {leves}\nAs pessoas acima de vinte anos são: {velhos}")
    
    # Continua (ou não) loop
    res = input("Deseja continuar?(s ou n): ").upper()
    
        
    
        
        
         