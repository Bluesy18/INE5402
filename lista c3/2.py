### 2 ###

from random import randrange

def verifica(t,escolha):
    while ((0 > escolha) or (escolha > t)):
        escolha = int(input("Número incorreto!! Digite novamente: "))
    return escolha 

def verifica2(modo):
    while (modo != "M") and (modo != "S"):
        modo = input("Modo inexistente! Digite novamente: ").upper()
    return modo

def modoMedia(escolha,t,soma):
    media= soma/t
    return media
    

soma = 0

t = int(input("Digite a ordem da matriz: "))

linha = [0] * t
matriz = [linha] * t
    
for i in range (t):
    linha = []
    for j in range (t):
        linha.append(randrange(0, 50))
        
    matriz[i] = linha
    
escolha = int(input("Digite a linha que você deseja fazer a operação: "))
escolha = verifica(t,escolha)

for p in matriz[escolha-1]:
    soma += p

modo = input("Se desejar a média, digite M. Se desejar a soma, digite S: ").upper()
modo = verifica2(modo)

print (matriz)

if modo == "M":
    res = modoMedia(escolha,t,soma)
else:
    res = soma
    
print(res)


