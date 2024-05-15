### 6 ###
from random import randrange

# Cria listas de jogo e resultado
jogo = []
resultado = []

# Usuário digita quantos jogos deseja fazer
n = int(input("Quantos jogos você deseja?: "))

# Cria jogos
for i in range(n):
    for j in range(6):
        jogo.append(randrange(60))
    resultado.append(jogo[:])
    jogo.clear()

# Mostra jogos        
for p in range(n):
    print(f"Jogo {p+1}: {resultado[p]}") 




        
    