#Davi Roberge Machado
#24100573

# Usuário digita quantidade de pessoas que passaram pelo sensor
n = int(input("Digite quantas pessoas passaram pelo sensor: "))

# Verifica se a quantidade é valida, caso não for, pede para digitar novamente
while ((n < 0) or (n > 10)):
    n = int(input("Valores inválidos! Tente novamente: "))

# Cria variável para somar "intersecções" nos instantes que a escada rolante está ligada
overlap = 0

# Cria loop baseado na quantidade de pessoas que passaram pelo sensor
for i in range(n):

    # Usuário digita o instante que a n pessoa passou pelo sensor
    t = int(input("Digite o instante que a pessoa passou: "))

    # Verifica se o instante é valido, caso não for, pede para digitar novamente
    while ((t < 0) or (t > 100)):
        t = int(input("Valores inválidos! Tente novamente: "))

    # Na primeira iteração, guarda o instante t
    if(i == 0):
        tpassado = t
        
    # Nas demais iterações...
    elif (i != 0):

        # Se intervalo entre instantes for menor que 10...
        if (t < tpassado + 10):
            # Calcula interseccção dos instantes
            overlap += ((tpassado + 10) - t)
        # Guarda instante t
        tpassado = t
            
# Mostra quanto tempo a escada rolante ficou ligada
print(f"A escada rolante ficou ligada por {(n*10) - overlap} segundos")
            
    
        
        
    
        
        