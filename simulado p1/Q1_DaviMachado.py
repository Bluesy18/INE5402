#Davi Roberge Machado
#24100573

# Usuário digita o número de instâncias desejadas
t = int(input("Digite o número de instâncias: "))

# Cria loop de acordo com o número de instâncias
for i in range (t):

    # Usuário digita a quantidade de consoantes e de dígitos
    c, d = map(int, input("Digite a quantidade de consoantes e de dígitos, respectivamente: ").split())
    
    # Verifica se os valores inseridos são válidos, caso não sejam, pede para digitar novamente
    while (0 > c) or (c > 6) or (0 > d) or (d > 9):
        c, d = map(int, input("Valores inválidos! Digite novamente: ").split())
        
    # Se valores forem ambos 0, o número de placas distintas é 0
    if ((c == 0) and (d == 0)):
        calc = 0
        
    else :

        # Calcula quantidade de possíveis placas distintas
        calc = (26**c)*(10**d)
    
    # Mostra quantidade de placas distintas
    print(f"A quantidade de placas distintas é de {calc}")
        
    
