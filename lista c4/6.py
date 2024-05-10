''' 6 '''
from random import randrange

jogo = []
resultado = []

n = int(input("Quantos jogos você deseja?: "))

for i in range(n):
    for j in range(6):
        jogo.append(randrange(60))
    resultado.append(jogo[:])
    jogo.clear()
        
for p in range(n):
    print(f"Jogo {p+1}: {resultado[p]}") 




        
    