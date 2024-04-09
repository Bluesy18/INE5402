#Davi Roberge Machado
#24100573

# Define função para encontrar números primos
def encontraPrimos(n):

    # Cria loop que decrementa 1, começando em n e indo até 2
    for j in range (n, 1, -1):

        # Variável de controle (0 == primo, 1 == não é primo)
        np = 0

        # Cria loop de 2 até j-1
        for k in range (2, j):

            # Divide j por k, a fim de descobrir se ele é divisível por algum número, se for, incrementa 1 na variável np e interrompe o loop
            if (j%k == 0):
                np += 1
                break

        # Se np continuar 0, o número é primo
        if (np == 0):
            pN = j
            break
        
    # Retorna número primo mais próximo
    return pN
        
# Usuário digita número de verificações
x = int(input("Número de verificações: "))

# Cria loop baseado no número de verificações
for i in range (x):

    # Usuário digita valores de N e M
    n, m = map(int, input("Digite os valores de N e M: ").split())
    
    # Verifica se os valores são válidos, se não forem, pede para usuário digitar novamente
    while ((n < 2) or (m > 100)):
        n, m = map(int, input("Valores incorretos! Digite novamente os valores de N e M: ").split())

    # p1 recebe valor de pN com o parâmetro n e p2 recebe valor de pN com o parâmetro m
    p1 = encontraPrimos(n)
    p2 = encontraPrimos(m)
    
    # Mostra o produto entre os primos mais próximos de N e M
    print(f"O produto entre os primos mais próximos de N e M é {p1*p2}")
    

        
    
    
